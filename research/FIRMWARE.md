# Firmware provenance and checksums

Target: Echo Show 5 Gen 3, H97N6S, `hypnos`, firmware build `7202000017420`.

| Artifact | SHA-256 | Notes |
|---|---|---|
| Signed parent U-Boot FIT | `157ef8534d4fbfcf85bd7c72c7c9ae7447e42086b3259fc5356c02af23ffcc93` | Used in original BL2 RSA/PSS experiments |
| BL2 | `d2e14618886c18736149fe323da074f1210a7250eab6a89d736034f2e091eba2` | Original ARM64 BL2 |
| Linux `boot.img` | `c0aff41d028badda0b2781a60e358080f0aa8929c2742d0b7ce83c63ea39ec0a` | 24,901,698 bytes in consolidated research archive |
| Extracted U-Boot stream `Inputs/uboot.bin` | `6118b031654ed34ee7a27703b60e920c6df99155fe7235ecc86d3e5d047ffda9` | 832,577 bytes; *different artifact* from signed parent FIT |

**Important:** Do not confuse the extracted U-Boot stream with the signed parent U-Boot FIT; their hashes refer to different byte streams.

Public firmware catalog: https://ftvdb.com/echo/firmware/com.amazon.hypnos.kepler.os/

No physical eMMC dump was acquired. Publicly distributed OTA firmware is not equivalent to a per-device storage image.

For copyright, safety and privacy reasons, vendor firmware binaries are not mirrored here. Researchers should independently obtain lawfully available firmware and verify the exact bytes before reproducing results. Never publish unique identifiers, credentials, production tokens, private signing keys, or user data.
