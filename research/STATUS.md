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

## November 15 synchronization — U-Boot entry points and FIT identity

The following results are from preserved offline research addenda; they are **not** retail-device tests. The complete evidence ZIPs are maintained in the shared ChatGPT Library folder `/echo show jail` and are not mirrored as vendor binaries in this public repository.

### Fastboot dispatch and production policy

- Original U-Boot SHA-256: `6118b031654ed34ee7a27703b60e920c6df99155fe7235ecc86d3e5d047ffda9`. The original dispatch-table audit decoded 15 command-name/handler pairs at file offsets `0x7d900–0x7d9ef`.
- The registered `boot`, `continue`, and `reboot` commands share a stub at `0x41e3c870` that follows a success-response path; **registration or an OKAY response does not prove execution of a downloaded image**.
- The command filter at `0x41e029e4` calls a production-policy predicate at `0x41e4ab38`. The latter consults `0x41e4a99c` and conditionally `0x41e0f308`. A nine-case original-opcode microexecution of `0x41e0f308` showed a short-circuit Boolean OR of two subordinate predicates, with their real data sources still unresolved.
- Later structural audits traced calls through `0x41e0f280`, `0x41e0f814`, and IDME-like getter `0x41e02ddc`. They do **not** establish an owner-accessible unlock state or the complete production transport behavior.
- A separate original-instruction audit of one-time authorization entry gates was preserved as `Echo_Gen3_One_Time_Auth_Entry_Gates_2026-11-13.zip`; it is **not** evidence of a valid credential, credential forgery, or retail unlock.

### FIT selection and rollback identity

- The boot routine uses a loader-selected configuration offset from `[x19,#0x68]` for later image-property lookups, while a second call to resolver `0x41e29a6c` feeds a `rollback-version` lookup. The second resolver's name argument originates from the same caller stack slot as the loader's earlier resolver argument.
- Original-instruction structural checks support these call/data-flow relationships. They do **not** establish mutation of the slot or name string, differing resolved offsets, or a successful authenticated-to-executed identity mismatch.
- Original-code Unicorn tests found `@` unit-name alias behavior in a synthetic renamed FIT, but that modification invalidated the original signature. Follow-up subimage-resolution tests on the authentic FIT resolved expected kernel, ramdisk and FDT references and rejected an absent reference. **The alias observation alone is not a signature bypass.**
- Original Linux `boot.img` SHA-256: `c0aff41d028badda0b2781a60e358080f0aa8929c2742d0b7ce83c63ea39ec0a`. Existing signed-FIT and payload-hash negative controls found no accepted unauthenticated executable payload.

### Remaining gaps

1. Prove or rule out loader-versus-rollback configuration disagreement with original-code execution and tracked name-buffer lifetime; retain negative controls.
2. Trace production Fastboot filter consumption and actual IDME/one-time-authorization storage provenance, without constructing or forging credentials.
3. Determine UART console availability and recovery entry/update authentication on retail hardware using non-destructive authorized observations.
4. Keep BL2, U-Boot FIT RSA, rollback, payload hashes, and retail fuse state as separate security barriers.

**Conclusion:** No demonstrated jailbreak, unauthorized Fastboot boot, credential bypass, or custom native-code execution.
