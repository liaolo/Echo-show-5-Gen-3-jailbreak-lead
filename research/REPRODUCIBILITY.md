# Evidence inventory and reproduction guide

## Preserved source collection

The consolidated November 13 research ZIP contains **214 entries** (nested archives, source scripts, logs, reports and two extracted firmware streams). Major top-level folders:

- `Session/Experiments/echo_dm_dependency_audit/`: native device-model/RSA emulation, authentic and negative tests
- `Session/Experiments/echo_higher_fit_auth/`: U-Boot higher FIT verifier and callback probes
- `Session/Experiments/echo_postselection_audit/`: post-selection verification-to-load static control flow
- `Session/Experiments/echo_crypto_init_review/`: SHA-256 context initialization, synthetic key tree, allocator probes
- `Session/Experiments/echo_key_selection_audit/`: key-selection tests
- `Session/Experiments/echo_unicorn_verify_audit/`: original ARM64 emulation probes
- `Session/Experiments/echo_bootvar_provenance/`: boot variables, slots and configuration provenance
- `Library/Archives/`: earlier independent evidence ZIPs
- `Library/Reports/`: reports and validation summaries
- `Inputs/boot.img`, `Inputs/uboot.bin`: extracted vendor firmware (not mirrored here)

Newer November 14 experiments retained in the shared research Library include:
- `Echo_Gen3_BL2_Original_RSA_Exponent_3_Cases_2026-11-14.zip`
- `Echo_Gen3_BL2_Original_RSA_PSS_Chained_4_Cases_2026-11-14.zip`
- `Echo_Gen3_All_Image_Coverage_Audit_2026-11-14.py` and JSON results
- `Echo_Gen3_Modified_Kernel_Check_2026-11-14.py` and JSON results
- `Echo_Gen3_FIT_Default_Selector_Audit_2026-11-14.py` and JSON results

**Current public release scope:** An index and findings, not a verified privacy-scrubbed mirror of all 214 entries. Do not assume any unlinked experiment script is already committed.

## Independent replication checklist

1. Acquire exact public `hypnos` firmware and verify artifact hashes in [FIRMWARE.md](FIRMWARE.md).
2. Separate the signed BL2 parent-U-Boot FIT verification from U-Boot's Linux `boot.img` verification.
3. Record every substituted callback and synthetic state, including memory allocator, device model and MMIO values.
4. Run authentic positive and corrupted-signature/digest negative controls with the same original-code pipeline.
5. Treat emulator-only behavior as emulator-only; do not claim retail fuse values or a working jailbreak.

## Public contribution safety

Before contributing logs/scripts, scan for home paths, emails, IP addresses, Wi-Fi credentials, device serial numbers, account tokens and private keys. Avoid committing vendor binaries or personal storage dumps. Provide hashes, minimized synthetic fixtures and reproducible steps where possible.
