# BL2: original ARM64 authentication experiments

**These are original-code Unicorn emulation results, not retail device observations or an unlock.** Source: four research ZIPs dated 2026-11-14 in the shared research archive. Public vendor binaries are omitted; original Python harnesses are retained in those archives pending source-by-source review.

## Artifact identity

- BL2 SHA-256: `d2e14618886c18736149fe323da074f1210a7250eab6a89d736034f2e091eba2`
- Signed U-Boot FIT SHA-256: `157ef8534d4fbfcf85bd7c72c7c9ae7447e42086b3259fc5356c02af23ffcc93`
- Signed FIT key path: `/signature/key-fit`

## Chained original RSA -> PSS (highest-value result)

| Control | Original RSA instructions | Original PSS instructions | PSS result |
|---|---:|---:|---|
| Authentic signature | 171,489 | 9,836 | flag=1; return=0 |
| Signature first byte corrupted | 171,489 | 65 | flag=0; return=-4 |
| Signature last byte corrupted | 171,489 | 65 | flag=0; return=-4 |
| Signed digest corrupted | 171,489 | 9,833 | flag=0; return=0 |

The signed digest for this experiment was obtained from an earlier original-region-builder test. Allocator/free services were substituted, while original RSA, Montgomery, PSS and MGF1 paths executed. This **does not** prove the complete BL2 wrapper, boot policy, or retail fuse state.

## Independent controls

- Original RSA exponentiation: three cases, each 171,489 original instructions and 19 Montgomery helper calls; outputs matched independent RSA calculations. Authentic trailer `0xbc`, corrupted-signature trailers `0x00` and `0x0c`.
- Original embedded-key parser: `key-fit` and `key-da` each parsed as 2048-bit keys; nonexistent node rejected with null output.
- Original PSS check: authentic and reordered-metadata controls accepted; digest-flipped, signature-flipped and invalid-trailer controls rejected (different return/flag semantics).

## Reproduction boundary

The original harness scripts reference local copies of `bl2.img` and `u-boot-mtk.bin`. Those proprietary firmware binaries are not mirrored. A complete standalone public harness package with all dependencies and audited fixtures is **not yet available**; the numerical results here are for independent review, not a claim of full reproducibility.

## Next checks

Trace the signed-region builder, embedded key parser, RSA/PSS callback and outer BL2 authorization wrapper end-to-end. Compare the emulated MMIO security selector with retail hardware evidence only if acquired. Do not infer an unlock from synthetic policy-bit experiments.
