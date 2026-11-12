# Echo Show 5 Gen 3 — Firmware and Custom Software Access Research

**Status: Research lead, NOT a working jailbreak.**

Independent, AI-assisted offline investigation of the Amazon Echo Show 5 **3rd generation (2023)**, model **H97N6S**, codename `hypnos`, MediaTek **MT8169**, focusing on firmware baseline **7202000017420**.

## Key findings

- **U-Boot FIT signature coverage:** Static evidence of old `hashed-nodes` behavior associated with CVE-2026-46728. This is **not** proof of a successful signature bypass or exploitable retail boot path.
- **Fastboot RAM boot:** A deferred callback and RAM-to-`bootm` path are present. The modeled locked-production command filter rejects ordinary `fastboot boot` before that callback is selected.
- **Manufacturer unlock:** Device-bound persistent and session-scoped signed authorization mechanisms are present in firmware. No public owner credential-issuance workflow was established.
- **Physical interface:** The J4 bottom contacts have no independently validated safe external data adapter or retail host transcript in the reviewed evidence.
- **Recovery and developer services:** Authenticated OTA/recovery and Vega-related binaries exist, but no documented owner native-package enrollment or arbitrary image installation workflow was found.
- **Legitimate extensions:** APL is documented for this generation; sandboxed HTML/JavaScript games are a plausible but unverified exact-model capability.

## Reports (chronological)

1. [Initial firmware security and feasibility](reports/01-initial-feasibility.md)
2. [Boot access and execution feasibility](reports/02-boot-access-and-execution.md)
3. [Locked boot policy and non-invasive access](reports/03-locked-boot-policy.md)
4. [Final custom software access assessment](reports/04-final-access-assessment.md)

Read the **final assessment** for the most current qualifications. Earlier conclusions are preserved for provenance, including the corrected interpretation of the Fastboot RAM-boot handler.

## Reproducibility status

These four reports were recovered from the researcher's document library and published as documentation. The original Codex workspace evidence directories (`echo_research/`, `echo_boot_access/`, `echo_locked_policy/`, and `echo_final_access/`) **have not yet been uploaded to this repository**. Therefore this repository does not yet contain the original disassembly, signature-check scripts, fixtures, test outputs, or preservation manifests. Do not mistake paths mentioned in the reports for files available here.

No retail H97N6S hardware was tested, no modified firmware was booted, and no custom OS installation was demonstrated. The investigation was heavily AI-assisted and has not been independently peer-reviewed.

## References

- [U-Boot upstream FIT verification fix](https://github.com/u-boot/u-boot/commit/2092322b31cc8b1f8c9e2e238d1043ae0637b241)
- [U-Boot FIT signature documentation](https://docs.u-boot.org/en/latest/usage/fit/signature.html)
- [Public hypnos firmware catalog](https://ftvdb.com/echo/firmware/com.amazon.hypnos.kepler.os/)
- [Exact-generation community Fastboot/J4 discussion](https://www.reddit.com/r/hacking/comments/1d01lf4/alexa_echo_show_5_3rd_gen_jailbreak_press_all/)

## Contributions and corrections

Independent verification, exact-model documentation, legitimate native developer-enrollment information, and safe non-invasive interface evidence are welcome. Please distinguish **static code evidence**, **simulated behavior**, and **observed retail hardware behavior**. Avoid posting account identifiers, private credentials, or unverified contact pin assignments.

## Responsible research

The goal is to document reproducible firmware-security findings and legitimate owner software-access possibilities, not to claim an existing jailbreak.
