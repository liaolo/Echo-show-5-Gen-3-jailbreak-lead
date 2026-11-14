# Contributing

We welcome independent reverse-engineering review of the Amazon Echo Show 5 Gen 3 (`hypnos`) boot chain.

## Useful contributions

- Cross-check original BL2 FIT signed-region construction and complete outer wrapper against the preserved four-case RSA/PSS results.
- Review U-Boot `loadcfg` selection, default metadata and the verification-to-execution FDT handoff.
- Reproduce authentic acceptance and corrupted-signature rejection with original U-Boot native crypto and document synthetic initialization.
- Provide exact-model, non-invasive hardware observations with safe electrical methodology and no personal/device-unique information.
- Compare independently acquired Echo Spot 2024 `baklava` firmware only after verifying its actual bootloader architecture.

## Reporting standard

Each result should state: firmware hash, target binary, entry point, input bytes or hashes, substitutions/stubs, exact positive/negative controls, outcome, limitations and reproduction steps. Label **static**, **emulator-only**, **retail observed**, or **hypothesis**.

Do not submit account credentials, device identifiers, serial numbers, full personal eMMC dumps, proprietary signing secrets or unreviewed firmware bundles. A vulnerability hypothesis is not a demonstrated exploit.
