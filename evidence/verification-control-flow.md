# Conditional post-selection branch map

```text
FIT loader 0x41e29bfc
    |-- runtime verify state [x27,#0x138] at 0x41e29da8
    |      |-- state 0 -> skip required config signature
    |      `-- nonzero -> 0x41e2ae04 required config verification
    |                    nonzero -> loader error -13
    |                    zero -> continue
    |-- same state [x27,#0x138] at 0x41e29e44
    |      |-- state 0 -> skip 0x41e296c8 image hash verifier
    |      `-- nonzero -> hash verifier, Boolean-like result
    |                       0 -> loader error -13
    |                       nonzero -> continue
    `-- 0x41e29eb8 -> 0x41e298dc architecture compatibility
          0 -> image loading error; nonzero -> later processing
          architecture getter is 0x41e28544, 'arch', not 'os'

Outer boot 0x41e20520 -> loader above
    loader negative -> outer error
    loader nonnegative -> config re-resolution 0x41e20550
    config negative -> outer error
    config nonnegative -> rollback version check at 0x41e2058c
       check nonzero -> log warning -> rollback lock at 0x41e205a0
       check zero -> rollback lock at 0x41e205a0
           lock nonzero -> log warning -> retry lock operation
           lock zero -> additional boot-time image preparation
    additional boot-time metadata, architecture, load, entry checks
    eventual OS entry decision not modeled in this bounded report
```

Distinguish the root FIT signature-verification result convention from the Boolean-like image hash helper and from image-architecture compatibility. It is incorrect to count `0x41e298dc` as a second image-hash operation. The conditional branch involving the runtime `verify` field does not establish that the field can be changed or persisted on a production device.
