# Echo Show 5 Gen 3 — Final Custom Software Access Assessment

12 November 2026, Israel. H97N6S / hypnos / MediaTek MT8169. Firmware baseline: 7202000017420. Continuation of *Locked Boot Policy and Non-Invasive Access*, not a replacement for its evidence.

**No new route to owner-controlled native execution, custom kernel boot, or persistent replacement OS was established.** The final pass did identify an important qualification: Amazon documents restricted skill presentations on this exact generation, and a separate sandboxed HTML/JavaScript game interface merits one small device-capability test. Neither supplies a native package installer or boot authorization.

**Decision: pause further offline boot-access analysis. Seek exact-model manufacturer/community evidence before buying hardware for native execution.** A borrowed unit could answer the restricted HTML question without opening it. That test is optional and does not reopen the bootloader investigation.

## A. New discoveries

### A1. An exact-generation restricted extension is documented

Amazon's APL known-issues page explicitly names **Echo Show 5 (3rd Gen, 2023 release)** and discusses its APL version reporting [S1]. This is stronger than a generic Echo Show product-family reference: it establishes documented APL presentation support on the generation under investigation. It does not establish the current APL version of baseline 7202000017420 or prove that the historical reporting bug persists.

Amazon separately documents testing development skills on an Echo associated with the developer's Amazon account, with a matching skill/device locale [S2]. Together these provide a legitimate path for owner-created skill presentations, subject to account, locale and service availability. No physical test was performed here. Skill backend execution must not be confused with native code running on the display.

Reproduction: inspect the exact-model entry in [S1], then use the documented skill-testing process in [S2]. A live `supportedInterfaces` response and on-screen presentation would supply unit-specific confirmation. No skill was built or deployed during this investigation.

### A2. The HTML game interface is a concrete, separately testable candidate

Amazon's current Web API for Games overview lists Echo Show devices as supported [S3]. Its device-side web runtime can execute developer-supplied HTML/JavaScript games. However, the implementation guide explicitly requires checking `Alexa.Presentation.HTML` in the requesting device's `supportedInterfaces` before launching [S4]. **APL support does not establish HTML support.** No H97N6S request transcript or matching-firmware game demonstration was obtained.

The documented scope is restricted: games only, HTTPS delivery, session-based execution, no local-file API or local storage, and no browser microphone/camera capture [S5]. This is a possible legitimate route to local sandboxed JavaScript, not arbitrary native executables, privileged services or startup persistence. Exact-model availability remains **plausible but unverified**.

Reproduction criterion: an identifiable H97N6S reports the HTML interface and successfully runs an ordinary compliant sample game through the documented skill flow. A browser test or simulator alone does not qualify.

### A3. The commercial USB-C stand does not establish a data route

Amazon's compliance document explicitly associates stand **CA9TR4** with **H97N6S** and describes its USB-C socket as a 7.5 W charging output [S6]. This closes a plausible accessory lead: a compatible commercial accessory exists, but the reviewed specification does not document a host-data bridge or service connection. It is not evidence of J4 connectivity. No electrical claim that data pins are physically absent is made.

### Searches that produced no new access evidence

Targeted searches for exact-model enrollment, service tools/manuals, pinouts, USB transcripts, source releases and independent boot-verifier reproduction produced no qualifying new result. The checked firmware catalog still lists four records, highest build 7202000017420 [S7]; no newer cataloged revision changed the baseline. That catalog is not a complete history of every Amazon deployment.

The original Fastboot/J4 and serial reports remain observations without a validated retail data connection [S8, S9]. The accessible Amazon source notice still exposed no downloadable matching archive in the retrieved rendering [S10]. Reviewed community project support lists identify other models, not hypnos [S11, S12]. These are bounded negative search results, not proof that private research or unpublished service equipment does not exist.

## B. Candidate access routes

Confidence describes the evidence boundary, not a probability of eventual unlocking. “Not established” means no reproducible owner workflow was found.

| Mechanism | Evidence | Owner accessibility | Authorization requirement | Possible execution scope | Current blocker | Confidence |
|---|---|---|---|---|---|---|
| APL development skill | Exact-generation Amazon documentation [S1]; account-based testing [S2] | Documented skill workflow; exact unit untested | Developer/account association, enabled skill, supported locale/service | Declarative presentation and permitted interactions; backend elsewhere | Unit/account availability unmeasured; no native deployment | High for documented generation support |
| Web API for Games | Echo Show family support [S3]; mandatory capability check [S4] | Conditional on real device advertising HTML | Skill development/account authorization and game policy | Sandboxed local HTML/JavaScript | Missing H97N6S capability transcript and demonstration | Medium; exact model unverified |
| Native Vega VDA/VSH/VPM | Preserved firmware services and gates; official enrollment is for Fire TV [S13] | No H97N6S owner enrollment established | Device enablement and host/package authorization | Native/package access if legitimately provisioned | No exact-model activation/eligibility procedure | High for installed infrastructure; unknown owner eligibility |
| Manufacturer persistent/session unlock | Prior binary evidence: signed, device/session-bound authorization | No public issuance workflow found | Accepted manufacturer credential | May authorize compiled boot/service paths, subject to downstream checks | Credential eligibility/issuance and usable external transport | High for compiled validators; no owner access evidence |
| Ordinary Fastboot RAM boot | Existing dispatcher/callback/bootm trace | Displayed mode reported; host transport unverified | Production boot restriction or accepted authorization | Conditional temporary boot | Both authorization and safe transport unresolved | High static evidence; no hardware demonstration |
| Rescue OTA / recovery / stock OTA | Existing service units, ACE OTA imports and authenticated updater | Normal stock recovery/update may be available; no arbitrary-image selection documented | Vendor update trust and boot policy | Vendor-selected/signed recovery software | No owner-image input or native-package entitlement established | High for known components; incomplete recovery behavior |
| BL2 download agent | Existing authenticated DA evidence | No non-invasive owner session demonstrated | Early-stage agent authorization | Service/provisioning operations, not a public development entitlement | Transport, credentials and exact permitted operations | Static evidence only |
| J4 factory contacts | Exact-model owner reports [S8, S9] | No validated external adapter | Protocol and authorization unknown | Unknown; contacts alone prove no execution scope | Electrical/protocol identification and no-opening compatibility | High confidence that access remains unestablished |
| CA9TR4 USB-C stand | Exact-model official charging specification [S6] | Commercial accessory | None for charging | Documented charging only | No documented data/service function | High for published scope |
| Other native projects / older Echo tools | Explicit other-model support lists [S11, S12] | Available for named supported products | Their model-specific prerequisites | Custom software on those products | No H97N6S support or reproducible transfer | High for model distinction |

Generic browser content, home cards and video-skill renderers do not add evidence of native package access. Fire TV VDA enrollment and Echo skill testing are distinct authorization systems; neither constitutes a bootloader unlock credential.

## C. Corrections and qualifications

1. **Qualify any broad statement that owners cannot supply custom software/content at all.** APL is documented on this generation. HTML game code is a concrete restricted candidate. The defensible negative conclusion concerns owner-controlled **native deployment and custom boot**, not all extensibility.
2. **Do not upgrade family-level HTML support to an H97N6S demonstration.** Amazon's own capability check is the deciding observation. Current generic support wording is a lead, not a retail transcript.
3. **Do not turn a charging stand into a data adapter.** Official H97N6S compatibility establishes mechanical/power compatibility only in the reviewed document.
4. **No new evidence warrants changing the prior production-policy model.** The production status remains a computed runtime predicate, not a measured fuse here. Neither its alternate states nor installed developer binaries establish an owner-selectable exception. This pass did not perform a new exhaustive caller audit and does not claim one.
5. **Preserve the deferred RAM-boot correction.** The older acknowledgement-only inference remains withdrawn. The callback exists; production dispatch authorization, transport and downstream checks remain separate conditions.
6. **Rescue OTA is not a demonstrated local installer.** The preserved path unit watches a local failure-manager marker and starts a system service. Imported ACE OTA functions establish update integration, not an owner-supplied image parameter or unauthenticated network endpoint. No public supported local package-selection workflow was found. This does not prove every recovery branch has been audited.

The FIT coverage lead remains an established static finding of the previous investigation. No new independent matching-firmware reproduction or retail acceptance evidence was located. No fresh CVE assessment, signature verification or payload test is represented as completed in this pass.

## D. Final feasibility assessment

| Question | Classification | Answer for an ordinary locked retail owner |
|---|---|---|
| Can the owner run an independently installed native application? | **Unsupported by current evidence** | No documented exact-model enrollment or deployment route was established. Installed native developer tooling is insufficient. |
| Can the owner temporarily boot a custom kernel? | **Unsupported by current evidence** | A RAM-boot implementation exists, but no permitted owner delivery/authorization chain is demonstrated. The narrower claim that ordinary `fastboot boot` is available in the modeled locked state is **contradicted by current evidence**. |
| Can the owner install a persistent custom OS? | **Unsupported by current evidence** | No demonstrated owner-authorized write, trusted boot and update/persistence chain. Temporary execution, even if later demonstrated, would not establish this. |
| Is any of those three outcomes demonstrated on H97N6S? | **Unsupported by current evidence** | No independently reproducible exact-model demonstration located. This is not a proof of technical impossibility. |
| Is a purchase justified for native/custom-OS research with no opening, probing or soldering? | **Unsupported by current evidence** | Not recommended for that objective. No presently validated non-invasive bootloader connection or native enrollment experiment justifies the purchase. |
| Can an owner create a restricted skill presentation? | **Supported but authorization-dependent** | Exact-generation APL documentation plus the documented account/locale testing process support this narrower outcome. Not tested on a physical unit here. |
| Can this unit run owner-authored sandboxed HTML game logic? | **Plausible but unverified** | A family-level documented mechanism exists; the exact unit must advertise HTML and run the sample. |

**Technical capability:** the firmware contains native services and conditional boot machinery; the hardware is not incapable of running other software in principle. **Amazon's security policy:** native development, service credentials, updates and boot acceptance have separate trust boundaries. **Ordinary owner access:** a documented skill workflow exists; no corresponding H97N6S native-enrollment or custom-boot workflow was established.

Persistence requires more than one successful process launch: a permitted installation location, service/startup entitlement, filesystem-integrity compatibility, accepted boot state, rollback compliance and survival through the A/B update lifecycle. The previous evidence documents barriers, not a complete authorized deployment recipe. Session web execution does not meet those persistence conditions.

## E. Minimum evidence needed for progress

Ranked by how directly it would change the native/custom-boot assessment; five maximum:

1. **An official H97N6S native developer enrollment workflow, or a reproducible authorized native-package install on a locked retail unit.** Required: exact model/build, eligibility, documented authorization steps and a benign owner-created native program actually executing. This could avoid the bootloader problem entirely.
2. **An exact-model owner-accessible manufacturer authorization/service process.** Required: published eligibility and credential issuance, permitted operations, and confirmation that owner software—not only vendor recovery—is allowed. Credential-validator code alone does not count.
3. **A validated no-opening external data connection.** Required: H97N6S board/revision applicability, connector electrical specification, safe compatible adapter and repeatable host enumeration/read-only protocol transcript. It would establish communication, not permission to boot.
4. **An independent end-to-end exact-model execution report.** Required: original firmware fingerprints, reachable legitimate input route, live authorization conditions, benign owner code demonstration, and a clear temporary-versus-persistent result. An offline signature-coverage observation alone does not qualify.
5. **Matching released source or a demonstrably changed firmware policy that exposes a supported owner route.** Required: source/build correspondence or original binary comparison, relevant policy change and documented retail reachability. Another version string or additional unexamined code is insufficient.

### The single most useful safe device observation

**On an already available or borrowed H97N6S, inspect the request capabilities from a normally enabled development skill, then—only if HTML is advertised—run a compliant official sample game.** This targets the only newly identified execution candidate with an ordinary account-based entry point. It tests restricted execution, not native access.

Using normal menus, Wi-Fi and supplied power:

1. Record the retail model label, displayed software/build, date, device language and account marketplace. Photograph identifying information with serial/account details redacted. This tests whether the observation concerns H97N6S and the stated baseline rather than a similarly named device.
2. Use the documented same-account development-skill process and matching locale [S2]. Capture only the relevant `supportedInterfaces` and viewport data; omit access tokens, account and device identifiers. Check APL and HTML separately [S4, S14]. This tests whether the unit actually exposes each restricted runtime. A simulator request is not evidence about the device.
3. If HTML is present, launch a small official sample game through its normal skill mechanism. Record a screen response to a touch plus a corresponding runtime message, with model/build provenance. Capability advertisement alone is weaker than this execution observation. If absent, stop this branch; it is not a reason to alter firmware or authorization.

A successful result would demonstrate sandboxed game execution on that unit only. A failure might reflect account/locale, service or sample configuration; preserve the failure rather than declaring the hardware incapable. This is not a purchase recommendation or a promise that a particular account in Israel is eligible. No skill, account or device was accessed during this investigation.

| Observation category | What would reduce uncertainty | Current action |
|---|---|---|
| Normal menus and supplied accessories | Exact model/build plus the capability/sample observation above | Possible on an existing unit; no factory reset or service-mode experiment needed |
| Verified external data connector | Read-only enumeration and documented identity/status queries would test real bootloader transport and live state | Deferred: no qualifying H97N6S adapter/connection established. The charging stand is not evidence of one. |
| Outside owner constraints | Internal UART, soldering, pad probing, unknown-contact cabling, storage access | Excluded. No pin assignments or connection instructions proposed. |

For a strictly native-only objective, the capability test does not remove a blocker. The highest-value next action is evidence from Amazon or an existing exact-model researcher, not purchasing a unit to rediscover a Fastboot screen.

## F. Stop-or-continue decision

**Pause the offline boot investigation and seek manufacturer/community evidence. Do not purchase this model expecting native custom software under the stated constraints.** There is no specific unexamined static lead here that plausibly supplies both owner authorization and non-invasive access. More disassembly by itself would not answer whether an owner can obtain either.

Continue only if one of E1–E5 arrives. Separately, the small HTML capability/sample test is worthwhile if an existing owner can perform it and restricted game execution is relevant. It could settle a limited legitimate extension path without changing the negative native/custom-OS assessment.

No new finding materially improves **native execution or custom boot feasibility**. The material qualification is that restricted custom presentation is documented, and local sandboxed game execution deserves an exact-model check. These should not be advertised as a jailbreak.

## Evidence provenance and preservation

The prior authoritative report and three evidence collections were retained unchanged. This pass compared **625 original-research manifest entries, 105 boot-access entries and 39 locked-policy entries**: no missing/changed entries. All three preserved ZIP hashes matched. This is an artifact-preservation check, not repeated firmware signature verification. Results: `echo_final_access/PRESERVATION_CHECK.json`; reproducible read-only script: `echo_final_access/verify_preservation.py`.

Relevant pre-existing anchors, cited rather than reanalyzed:

| Question | Existing precise reference |
|---|---|
| Production and accepted-unlock policy | `echo_locked_policy/production-policy.txt`, `production-state.txt`, `unlock-state.txt`; functions `0x41e4ab38`, `0x41e4a99c`, `0x41e0f308` |
| Initial command decision | `echo_locked_policy/command-filter.txt`; predicate `0x41e029e4`, normalization `0x41e4ac84` |
| Deferred RAM boot | `echo_locked_policy/ram-completion.txt`, `ram-callback.txt`, `ram-boot.txt`; callback `0x41e512f4` → `0x41e3bd60` → fallback bootm |
| Verification and runtime qualifications | `echo_locked_policy/verify-state.txt`, `signature-checks.txt`, `rollback-policy.txt`; report sections 3 and 6 |
| Rescue OTA trigger | `echo_boot_access/system-policy/lib/systemd/system/rescueOTA.path` and `rescueOTA.service` |
| Rescue OTA API imports | `echo_boot_access/binary-strings/usr/lib/librescueOTAservice-priv.so.symbols.txt`: `aceOta_start`, `aceOta_forceUpdate`; `startOtaWithRetry` symbol `0x14cb9`, size 1268, is a Thumb-marked address, not an execution observation |
| VDA/VSH/VPM and update authorization | Prior boot-access report and preserved `echo_boot_access/system-policy/` service/config evidence |

U-Boot addresses above use the prior payload link base `0x41e00000`; payload SHA-256 `6118b031654ed34ee7a27703b60e920c6df99155fe7235ecc86d3e5d047ffda9`. The enclosing `u-boot-mtk.bin` has a different hash; do not interchange the two artifacts.

No firmware extraction, cryptographic re-verification, altered image, authorization change, exploit construction or device interaction occurred. The search was focused and public; no private service documentation or paywalled teardown was accessed. New evidence notes and search boundaries are saved separately under `echo_final_access/`.

## Primary sources and reference records

- **S1:** Amazon, [APL Known Issues](https://developer.amazon.com/en-GB/docs/alexa/alexa-presentation-language/apl-known-issues.html), exact-generation entry. Retrieved lines 291–293 identify the model; not a baseline-specific measurement.
- **S2:** Amazon, [Test and Debug Your Skill](https://developer.amazon.com/en-US/docs/alexa/test/test-your-skill-overview.html), account/locale testing, retrieved lines 503–540.
- **S3:** Amazon, [About Alexa Web API for Games](https://developer.amazon.com/en-US/docs/alexa/web-api-for-games/alexa-games-about.html), supported-device family wording, retrieved lines 545–553.
- **S4:** Amazon, [Build Your Alexa Skill for Web App Games](https://developer.amazon.com/en-US/docs/alexa/web-api-for-games/alexa-games-build-your-skill.html), HTML capability check. Also [HTML interface](https://developer.amazon.com/en-GB/docs/alexa/web-api-for-games/alexa-presentation-html-interface.html).
- **S5:** Amazon, [Build Your Web App](https://developer.amazon.com/en-US/docs/alexa/web-api-for-games/alexa-games-build-your-webapp.html), game-only requirement and sandbox restrictions, retrieved lines 478–493 and 558–579.
- **S6:** Amazon, [CA9TR4 stand safety/compliance](https://digprjsurvey.amazon.com/csad/help/node/TgMAMTCMApD4fFcyEq), H97N6S compatibility and charging specification, retrieved lines 13–15 and 38–48.
- **S7:** FTVDB, [hypnos firmware history](https://ftvdb.com/echo/firmware/com.amazon.hypnos.kepler.os/), public catalog metadata; not a manufacturer guarantee of complete release coverage.
- **S8:** Original owner, [exact-model Fastboot/J4 report](https://www.reddit.com/r/hacking/comments/1d01lf4/alexa_echo_show_5_3rd_gen_jailbreak_press_all/). Uncalibrated measurements and a screen report are not a validated pinout.
- **S9:** Original researcher, [third-generation serial-data report](https://www.reddit.com/r/hacking/comments/1g9zi04/echo_show_5_3rd_gen_serial_data/). Observed serial-looking signals; no established usable console in the reviewed report.
- **S10:** Amazon, [Echo source-code notice](https://digprjsurvey.amazon.com/csad/help/node/201626480). Retrieved rendering announces source availability but exposes no matching archive link.
- **S11:** Project author, [TECHO5 supported models](https://github.com/HuskerMinion/techo5/blob/main/README.md). Support table does not include hypnos; broad claims about all public research are not adopted as proof.
- **S12:** Project author, [LibreEcho supported targets](https://github.com/aslater3/LibreEcho/blob/main/docs/install/README.md). Reviewed installation targets are older MT8163 devices; no procedure is transferred to H97N6S.
- **S13:** Amazon, [Enable Vega Developer Mode](https://developer.amazon.com/docs/vega/2.0/developer-mode), explicitly Fire TV prerequisites and enrollment. Not evidence of Echo eligibility.
- **S14:** Amazon, [Configure APL support](https://www.developer.amazon.com/en-US/docs/alexa/alexa-presentation-language/apl-support-for-your-skill.html), APL capability checks and RenderDocument.

This report adds a bounded documentation finding and a stopping decision. All prior detailed binary, signature and boot-policy conclusions retain their earlier scope and qualifications.