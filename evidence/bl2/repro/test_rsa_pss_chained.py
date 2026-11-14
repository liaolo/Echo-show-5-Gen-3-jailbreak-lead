import struct,hashlib,json,pathlib
from unicorn import Uc,UC_ARCH_ARM64,UC_MODE_ARM,UC_HOOK_CODE
from unicorn.arm64_const import *
import struct,hashlib,json, pathlib,time
from unicorn import Uc,UC_ARCH_ARM64,UC_MODE_ARM,UC_HOOK_CODE
from unicorn.arm64_const import *
B=pathlib.Path(__file__).with_name('bl2.img').read_bytes();F=pathlib.Path(__file__).with_name('u-boot-mtk.bin').read_bytes()
assert hashlib.sha256(B).hexdigest()=='d2e14618886c18736149fe323da074f1210a7250eab6a89d736034f2e091eba2'
def parse(d):
 so,strings=struct.unpack_from('>II',d,8);size=struct.unpack_from('>I',d,36)[0];i=so;stack=[];out={}
 while i<so+size:
  tok=struct.unpack_from('>I',d,i)[0];i+=4
  if tok==1:
   e=d.index(b'\0',i);stack.append(d[i:e].decode());i=(e+4)&~3
  elif tok==2:stack.pop()
  elif tok==3:
   length,nameoff=struct.unpack_from('>II',d,i);i+=8;e=d.index(b'\0',strings+nameoff);name=d[strings+nameoff:e].decode();path='/'+'/'.join(v for v in stack if v);out.setdefault(path,{})[name]=bytes(d[i:i+length]);i=(i+length+3)&~3
  elif tok==4:pass
  elif tok==9:break
  else:raise ValueError((tok,i))
 return out
props=parse(F)['/configurations/conf-1/signature-1'];sig=props['value'];key=parse(B[0xcf0:])['/signature/key-fit'];n=int.from_bytes(key['rsa,modulus'],'big');e=int.from_bytes(key['rsa,exponent'],'big');expected=pow(int.from_bytes(sig,'big'),e,n).to_bytes(256,'big')
BASE=0x200000;CODE=BASE+0x710;FDT=0x10000000;WORK=0x11000000;RET=0x12000000

# The parser, key-fitting data and modulus/exponent are initialized by the preamble.
assert e==65537
cases=[('authentic_signature',sig),('signature_first_byte_corrupted',bytes([sig[0]^1])+sig[1:]),('signature_last_byte_corrupted',sig[:-1]+bytes([sig[-1]^1])),('signed_digest_corrupted',sig)]
results=[]
for label,signature in cases:
 u=Uc(UC_ARCH_ARM64,UC_MODE_ARM)
 u.mem_map(BASE,0x70000);u.mem_write(CODE,B);u.mem_map(FDT,0x10000);u.mem_write(FDT,B[0xcf0:0xcf0+0x611]);u.mem_map(WORK,0x40000);u.mem_map(RET,0x1000)
 out=WORK+0x1000;cnt=WORK+0x5000;stack=WORK+0x3e000
 for reg,val in [(UC_ARM64_REG_X0,out),(UC_ARM64_REG_X1,FDT),(UC_ARM64_REG_W2,0x28),(UC_ARM64_REG_X3,cnt),(UC_ARM64_REG_SP,stack),(UC_ARM64_REG_X30,RET)]:u.reg_write(reg,val)
 u.emu_start(CODE+0x43380,RET,count=100000)
 raw=u.mem_read(out,0x30)
 assert struct.unpack_from('<I',raw,0x24)[0]==2048
 for ptr_off in (0,8):
  ptr=struct.unpack_from('<Q',raw,ptr_off)[0];b=bytes(u.mem_read(ptr,256));newptr=WORK+0x12000+ptr_off*0x100
  u.mem_write(newptr,b[::-1]);u.mem_write(out+ptr_off,struct.pack('<Q',newptr))
 inp=WORK+0x9000;dest=WORK+0xa000;u.mem_write(inp,signature[::-1]);u.mem_write(dest,bytes(256))
 for reg,val in [(UC_ARM64_REG_X0,dest),(UC_ARM64_REG_X1,inp),(UC_ARM64_REG_X2,out),(UC_ARM64_REG_SP,stack),(UC_ARM64_REG_X30,RET)]:u.reg_write(reg,val)
 ticks=[0];calls=[0]
 def hook(uc,pc,size,_):
  ticks[0]+=1
  if pc==CODE+0x49510:calls[0]+=1
  if pc==RET:uc.emu_stop()
 u.hook_add(UC_HOOK_CODE,hook)
 u.emu_start(CODE+0x4a5c0,RET,count=3000000)
 got=bytes(u.mem_read(dest,256))[::-1];expected=pow(int.from_bytes(signature,'big'),e,n).to_bytes(256,'big')
 # Continue within the SAME original BL2 emulator: endian-prep and feed original RSA output into original PSS checker.
 digest=bytes.fromhex('a0819590800ad02c090e41b82e97e08c9ab772b5235b9cfa03ec8553eb03410f')
 if label=='signed_digest_corrupted':digest=bytes([digest[0]^1])+digest[1:]
 digestptr=WORK+0x19000;encodedptr=WORK+0x1a000;flagptr=WORK+0x1b000
 u.mem_write(digestptr,digest);u.mem_write(encodedptr,got);u.mem_write(flagptr,b'\0'*4)
 for reg,val in [(UC_ARM64_REG_X0,digestptr),(UC_ARM64_REG_X1,32),(UC_ARM64_REG_X2,encodedptr),(UC_ARM64_REG_X3,256),(UC_ARM64_REG_X4,222),(UC_ARM64_REG_X5,2047),(UC_ARM64_REG_X6,flagptr),(UC_ARM64_REG_SP,stack),(UC_ARM64_REG_X30,RET)]:u.reg_write(reg,val)
 nxt=[WORK+0x21000];ticks_pss=[0];events=[]
 def pss_hook(uc,pc,size,_):
  ticks_pss[0]+=1
  if pc==CODE+0x14a70:
   pt=nxt[0];nxt[0]+=0x2000;uc.reg_write(UC_ARM64_REG_X0,pt);uc.reg_write(UC_ARM64_REG_PC,uc.reg_read(UC_ARM64_REG_X30));events.append('allocator')
  elif pc==CODE+0x14bd0:
   uc.reg_write(UC_ARM64_REG_PC,uc.reg_read(UC_ARM64_REG_X30));events.append('free')
  elif pc==CODE+0x4a720:events.append('original_mgf1')
  elif pc==RET:uc.emu_stop()
 u.hook_add(UC_HOOK_CODE,pss_hook)
 pss_error=None
 try:u.emu_start(CODE+0x4a810,RET,count=1000000)
 except Exception as ex:pss_error=str(ex)
 pss_return=u.reg_read(UC_ARM64_REG_W0);pss_return=pss_return if pss_return<0x80000000 else pss_return-0x100000000
 pss_flag=struct.unpack('<I',u.mem_read(flagptr,4))[0]
 result=dict(case=label,rsa_original_instructions=ticks[0]-ticks_pss[0],total_original_instructions=ticks[0],montgomery_helper_calls=calls[0],matches_independent_rsa=(got==expected),original_encoded_message_sha256=hashlib.sha256(got).hexdigest(),expected_encoded_message_sha256=hashlib.sha256(expected).hexdigest(),trailer_byte=got[-1],pss_trailer_valid=(got[-1]==188),pss_original_instructions=ticks_pss[0],pss_original_return=pss_return,pss_flag=pss_flag,pss_error=pss_error,pss_events=events)
 print(json.dumps(result));assert got==expected;results.append(result)
pathlib.Path(__file__).with_name('rsa_pss_chained.json').write_text(json.dumps({'bl2_sha256':hashlib.sha256(B).hexdigest(),'uboot_fit_sha256':hashlib.sha256(F).hexdigest(),'rsa_key':'/signature/key-fit','results':results},indent=2)+'\n')
