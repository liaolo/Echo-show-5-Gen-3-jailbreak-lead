# BL2 original RSA -> PSS reproducibility harness

This directory contains the original `test_rsa_pss_chained.py` harness from `Echo_Gen3_BL2_Original_RSA_PSS_Chained_4_Cases_2026-11-14.zip`, reproduced as source code rather than as a summary.

## Inputs

Put `bl2.img` and `u-boot-mtk.bin` next to the script. These are **extracted from the public vendor firmware**, not a retail-device eMMC dump. Vendor binary files are not included here.

- `bl2.img` SHA-256: `d2e14618886c18736149fe323da074f1210a7250eab6a89d736034f2e091eba2`
- `u-boot-mtk.bin` signed FIT SHA-256: `157ef8534d4fbfcf85bd7c72c7c9ae7447e42086b3259fc5356c02af23ffcc93`

Note that `u-boot-mtk.bin` here is the **signed FIT**, not the separate extracted U-Boot executable whose SHA-256 begins `6118b031`.

## Run

```bash
python -m pip install unicorn
python test_rsa_pss_chained.py
```

The script writes `rsa_pss_chained.json` in its directory. Compare the four case records to `../../chained-four-controls.json`.

## Limitations

- Hard-coded original-code offsets are tied to the above BL2 hash.
- Allocator and free callbacks are substituted with emulator stubs; the original RSA, Montgomery and PSS/MGF1 code runs.
- The signed digest is a fixture from a prior region-builder experiment, not recomputed end-to-end here.
- This does not emulate the entire boot chain or establish the security fuse state on a retail Echo Show.
- The script is published as preserved source; this GitHub publication step did **not** rerun it.
