# Research status — 2026-11-14

## Evidence levels

**Confirmed in offline original-code emulation:** BL2's original key parser, RSA exponentiation and PSS verification chain accepts an authentic signed parent U-Boot FIT and rejects signature/digest corruption in four controls. The authentic RSA run involved 171,489 original ARM64 instructions; authentic PSS verification 9,836. Only allocator/free services were stubbed in the combined subroutine experiment. The signed-region digest was provided from a prior original-region-builder experiment. **This is not the full BL2 wrapper or a real device run.**

**Confirmed static FIT coverage:** Eight Linux boot configurations have signed kernel, ramdisk and selected FDT hash references. The global FIT default selector is outside those signed regions. Whether production uses that default is unproven.

**Other original-code emulator results:** The higher U-Boot FIT wrapper and native RSA/device-model path were explored in distinct runs. An early native callback fault at `0x41e6fe18` wrote through a null SHA-256 context pointer; later synthetic provisioning avoided that crash. A separate archived original-native-crypto test reports authentic acceptance and signature-corruption rejection. These are not equivalent to a complete retail boot chain.

**Hypotheses only:** FIT verification-to-execution mismatch; configuration selection discrepancy; exploitable hashed-nodes handling; BL2 security-policy register manipulation. No working bypass established.

**Not tested:** Retail eFuse/MMIO state, real physical fastboot unlock, modified firmware execution, physical eMMC dump, custom OS boot.

## Notable BL2 security-policy lead

An original BL2 selector associated with descriptor `0x4B` accesses candidate MMIO `0xFFFF0000022B0060`, **bit 1**. In synthetic emulation, the selector branches differently according to that bit. Actual retail value and earlier BootROM protections are unknown. This is **not** a demonstrated secure-boot bypass.

## Current highest-value research

1. Execute original BL2 signed-region construction, key lookup, callback and outer FIT wrapper together with authentic and negative controls.
2. Audit original U-Boot configuration selection versus the configuration actually loaded/executed; compare verified FDT and selected FDT.
3. Reproduce and independently review the preserved native U-Boot RSA acceptance and rejection tests, documenting all synthetic dependencies.
4. Obtain an independently sourced `baklava` Echo Spot 2024 firmware image for read-only comparison; do not assume matching secure boot from shared Kepler OS.

## Caveat

The shared ChatGPT Library canonical status contains more detailed rolling research. This repository snapshot is a curated public handoff, not a replacement for the complete private research archive.
