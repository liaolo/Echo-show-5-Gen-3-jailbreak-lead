# Echo Show 5 Gen 3 — Firmware Security Research

**Status: active, AI-assisted offline research. No demonstrated jailbreak, unlock, modified-code boot, or retail hardware exploit.**

Target: Amazon Echo Show 5 (3rd generation, 2023), H97N6S, `hypnos`, MediaTek MT8169B, Vega/Kepler Linux. Baseline firmware build `7202000017420`.

## Start here

1. [Research findings and evidence matrix](research/STATUS.md)
2. [Reproduction and evidence inventory](research/REPRODUCIBILITY.md)
3. [Firmware provenance, hashes and safe acquisition](research/FIRMWARE.md)
4. [Open questions and contribution guide](research/CONTRIBUTING.md)
5. [Original four research reports](reports/)

## Key results

- Original BL2 ARM64 RSA public-key exponentiation and RSA-PSS verifier ran together in a Unicorn emulator. Authentic signed U-Boot FIT accepted; two corrupted signatures and a corrupted signed digest rejected. This is *not* the full original BL2 authorization wrapper.
- Original U-Boot FIT verifier was tested with authentic Linux `boot.img`; later archived native-crypto experiments progressed beyond an earlier null SHA-256 context crash. Separate experiments have different callback substitutions and must not be conflated.
- Eight signed FIT configurations were examined. Kernel, ramdisk and the **selected** device-tree hash are signed for each configuration.
- The FIT `default` selector is outside the signed regions. This does **not** demonstrate arbitrary-code execution; the retail configuration-selection path and downstream checks remain unresolved.
- A one-bit modification of the kernel changes its SHA-256 digest. No modified kernel was accepted or executed.

## Firmware and privacy policy

This public repository intentionally does **not** contain vendor firmware binaries, full eMMC dumps, device-unique credentials, private keys, account data or unreviewed bulk archives. The research derives from publicly catalogued Amazon firmware packages; see [firmware provenance](research/FIRMWARE.md). Researchers can independently acquire firmware through the referenced public catalog and verify hashes.

The available consolidated archive has 214 entries, including nested experiment archives, reports, scripts, JSON logs, `boot.img`, and U-Boot bytes. It is **not** a physical-device eMMC dump. We are publishing a curated, privacy-conscious evidence index first, rather than indiscriminately copying unknown binary or log content into a public repo.

## External references

- [Public hypnos firmware catalog](https://ftvdb.com/echo/firmware/com.amazon.hypnos.kepler.os/)
- [U-Boot FIT signing documentation](https://docs.u-boot.org/en/stable/usage/fit/signature.html)
- [Upstream FIT verification fix](https://github.com/u-boot/u-boot/commit/2092322b31cc8b1f8c9e2e238d1043ae0637b241)

Independent verification and corrections welcome. Distinguish confirmed original-code emulation, static inspection, hypotheses, and physical retail-device observations.
