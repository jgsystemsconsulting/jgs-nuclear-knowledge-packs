# Capability to Knowledge-Pack Map

Live working map. Working artifact mapping sector technical capabilities to the pack chapters that provide reference depth for each capability. Entries include support files.

Rules of construction:
- Every chapter in every pack under `packs/<slug>/chapters/` is assigned to exactly one capability cluster (best fit).
- Signpost packs contain no chapters and are not mapped.
- Machine-readable version: `docs/capability-pack-map.json`.
- Machine-readable classification rules: `docs/classification-rules.json`.
- Changelog (v0.1.0): live working map over packs under packs/.

## Summary

| Cluster | Entries |
|---|---|
| 1. Life Cycle & Requirements | 8 |
| 2. Verification & Testing | 2 |
| 3. Regulatory Framework & Staff Review | 25 |
| 4. Quality Assurance Criteria | 8 |
| 5. Risk-Informed Decisionmaking | 8 |
| 6. Cyber Security Programs | 8 |
| 7. Accident Monitoring | 8 |
| **Total** | **67** |

## 1. Life Cycle & Requirements

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nrc-nuclear | ch02-software-life-cycle-processes.md | RG 1.173 Rev 1 software life cycle processes and BTP 7-14 plan-level review of life cycle plans |
| nrc-nuclear | ch03-software-requirements-specifications.md | RG 1.172 Rev 1 software requirements specifications for software and complex electronics |
| nrc-nuclear | ch04-software-configuration-management-plans.md | RG 1.169 Rev 1 software configuration management plans and the BTP 7-14 CM plan review |
| nrc-btp-7-18-plc | ch02-software-vs-firmware-boundary.md | Where this pack draws the software versus firmware line, without unread BTP criteria |
| nrc-btp-7-18-plc | ch03-life-cycle-vs-btp-7-14.md | How PLC life-cycle questions leave this pack for nrc-nuclear BTP 7-14 chapters |
| nrc-btp-7-18-plc | ch06-documentation-set.md | Documentation-set questions as a life-cycle product list this pack does not invent |
| nrc-10cfr-part50-licensing-basis | ch02-50-34-contents-of-applications.md | 50.34 application contents: the preliminary and final safety analysis report categories |
| nrc-10cfr-part50-licensing-basis | ch03-50-36-technical-specifications.md | 50.36 technical specification categories and the four limiting-condition criteria |

## 2. Verification & Testing

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nrc-nuclear | ch05-verification-validation-reviews-audits.md | RG 1.168 Rev 2 verification, validation, reviews, and audits with the BTP 7-14 V&V plan review |
| nrc-nuclear | ch06-test-documentation-and-unit-testing.md | RG 1.170 Rev 1 test documentation and RG 1.171 Rev 1 unit testing with the BTP 7-14 test plan review |

## 3. Regulatory Framework & Staff Review

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nrc-nuclear | ch01-nrc-software-assurance-framework.md | How NRC Regulatory Guides, the SRP, and BTP 7-14 fit together for digital safety system software |
| nrc-nuclear | ch07-btp-7-14-staff-software-review.md | BTP 7-14 Rev 6 staff review of software implementation activities and design outputs |
| nrc-nuclear | ch08-endorsed-standards-and-adjacent-guidance.md | Endorsed IEEE and IEC standards, IAEA guides, and adjacent NRC documents by designation and edition only |
| nrc-nuclear | ch09-rg-1-152-pdd-criteria-and-sdoe.md | RG 1.152 Rev 4 criteria for programmable digital devices and the secure development and operational environment |
| nrc-nuclear | ch10-app-7-1-d-ieee-7-4-3-2-evaluation.md | NUREG-0800 Appendix 7.1-D Rev 1 staff evaluation of the application of IEEE Std 7-4.3.2 |
| nrc-nuclear | glossary.md (support file) | Software assurance terms used across the nrc-nuclear chapters |
| nrc-nuclear | cheatsheet.md (support file) | Decision rules routing software assurance questions to the right nrc-nuclear chapter |
| nrc-btp-7-18-plc | ch01-plc-role-in-safety-ic.md | What BTP 7-18 Rev. 6 is for in digital safety I&C, as orientation from the listing-page pin |
| nrc-btp-7-18-plc | ch04-commercial-dedication-touchpoints.md | Commercial-dedication questions this pack owns, with no invented dedication procedure |
| nrc-btp-7-18-plc | ch05-failure-modes-staff-eye.md | Staff-eye failure-mode questions as a review lens, not a test procedure |
| nrc-btp-7-18-plc | ch07-anti-patterns.md | Pack-use failures: quoting the BTP, citing unread sections, treating IEEE text as in-pack |
| nrc-btp-7-18-plc | ch08-rg-1-152-and-app-7-1-d.md | Pointers to nrc-nuclear ch09 and ch10 for RG 1.152 and Appendix 7.1-D |
| nrc-btp-7-18-plc | glossary.md (support file) | Terms this pack uses, IEEE and IEC designation only |
| nrc-btp-7-18-plc | cheatsheet.md (support file) | Edition rule, name-only rule, and which chapter owns the question |
| nrc-10cfr-part50-licensing-basis | ch01-part50-overview-and-definitions.md | Part 50 structure, license classes, and the 50.2 definitions a licensing question reaches for first |
| nrc-10cfr-part50-licensing-basis | ch04-50-54-conditions-of-licenses.md | 50.54 standing license conditions: quality program, operators, emergency plans, security, insurance |
| nrc-10cfr-part50-licensing-basis | ch05-50-59-changes-tests-experiments.md | 50.59 no-amendment change lane: definitions, two-condition gate, and eight screening criteria |
| nrc-10cfr-part50-licensing-basis | ch06-appendix-a-gdc-overview.md | Appendix A General Design Criteria as an index: six groups, criteria numbers and titles |
| nrc-10cfr-part50-licensing-basis | ch07-appendix-b-pointer.md | Appendix B pointer: scope sentence and the 50.34 and 50.54 hooks, criteria bodies left to the QA pack |
| nrc-10cfr-part50-licensing-basis | glossary.md (support file) | Licensing-basis terms this pack uses, keyed to the eCFR slices |
| nrc-10cfr-part50-licensing-basis | cheatsheet.md (support file) | Which chapter owns the question, the pin rule, and the licensing-basis limits |
| nrc-qa-rg-1-28 | ch07-licensing-hooks-part-50-52.md | QA program description in Part 50 and Part 52 license applications and the 50.54(a) license condition |
| nrc-risk-informed-rg-1-174 | ch07-implementation-monitoring-and-staff-review.md | Implementation and monitoring after decision and staff review framing at orientation level |
| nrc-cyber-rg-5-71 | ch07-the-part-73-shape-and-staff-review.md | Where 73.54 and RG 5.71 sit for civil power reactors; program documentation and staff review framing at framework level |
| nrc-accident-monitoring-rg-1-97 | ch07-regulatory-frame-and-staff-review.md | Regulatory frame and staff review orientation; specific variables and design detail directed to the guide; NUREG-0700 and IEEE 497 named only |

## 4. Quality Assurance Criteria

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nrc-qa-rg-1-28 | ch01-rg-1-28-role-and-app-b.md | RG 1.28 Rev 6 role: what the guide endorses for design and construction QA programs and how it relates to Appendix B |
| nrc-qa-rg-1-28 | ch02-app-b-to-nqa-1-bridge.md | Appendix B eighteen criteria as a names-only orientation list and how NQA-1 Part I requirements map onto them |
| nrc-qa-rg-1-28 | ch03-nqa-1-edition-pathway.md | The three NQA-1 editions Rev 6 endorses, named with owner ASME only and no standard text |
| nrc-qa-rg-1-28 | ch04-part-i-vs-part-ii.md | Part I and Part II requirements shape as RG 1.28 Rev 6 endorses them, described from NRC discussion only |
| nrc-qa-rg-1-28 | ch05-clarifications-and-positions.md | How RG 1.28 Rev 6 clarifications and regulatory positions condition the NQA-1 endorsement |
| nrc-qa-rg-1-28 | ch06-commercial-grade-nei-14-05a.md | NEI 14-05A Rev 1 name hook: accreditation in lieu of commercial grade surveys for laboratory calibration and test services |
| nrc-qa-rg-1-28 | glossary.md (support file) | QA program criteria terms this pack uses, keyed to the RG 1.28 Rev 6 orientation chapters |
| nrc-qa-rg-1-28 | cheatsheet.md (support file) | Which chapter owns the QA criteria question, the pin rule, and the not-advice limits |

## 5. Risk-Informed Decisionmaking

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nrc-risk-informed-rg-1-174 | ch01-rg-1-174-role-and-scope.md | RG 1.174 Rev. 3 role and scope: using PRA in risk-informed decisions on plant-specific licensing basis changes, pinned ML17317A256 |
| nrc-risk-informed-rg-1-174 | ch02-integrated-decisionmaking-framework.md | Integrated decisionmaking framework and the four stages, with PRA insights weighed beside defense-in-depth and safety margins |
| nrc-risk-informed-rg-1-174 | ch03-engineering-analysis-and-risk-metrics.md | Engineering analysis orientation; ΔCDF and ΔLERF named as the guide's change-in-risk metrics only, numeric tables stay in the guide |
| nrc-risk-informed-rg-1-174 | ch04-licensing-basis-and-50-59-connection.md | Licensing basis connection: the carried 50.59 two-limb gate, minimal-increase wording, and FSAR as updated baseline, orientation only |
| nrc-risk-informed-rg-1-174 | ch05-defense-in-depth-and-safety-margins.md | Defense-in-depth, safety margins, and performance-based consideration as framework considerations through the change |
| nrc-risk-informed-rg-1-174 | ch06-uncertainty-and-pra-adequacy-hooks.md | Uncertainty and PRA technical adequacy as named considerations; RG 1.200 Rev 3 and NUREG-1855 name hooks, no criteria or methods |
| nrc-risk-informed-rg-1-174 | glossary.md (support file) | Risk-informed decisionmaking terms this pack uses, keyed to the RG 1.174 Rev. 3 orientation chapters |
| nrc-risk-informed-rg-1-174 | cheatsheet.md (support file) | Which chapter owns the risk-informed change question, the pin rule, and the no-numeric-value limits |

## 6. Cyber Security Programs

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nrc-cyber-rg-5-71 | ch01-rg-5-71-role-and-scope.md | RG 5.71 Rev. 1 role and scope: cyber security programs for nuclear power reactors, pinned ML22258A204, guide character orientation |
| nrc-cyber-rg-5-71 | ch02-10-cfr-73-54-the-regulation.md | 10 CFR 73.54 at orientation level from public eCFR text; protection goal stated without control detail; named-site programs named out |
| nrc-cyber-rg-5-71 | ch03-cyber-security-program-shape.md | Graded, defense-in-depth program shape; defensive controls named as categories only, no product or tuning guidance |
| nrc-cyber-rg-5-71 | ch04-defensive-architecture-and-defense-in-depth.md | Defensive architecture as mutually reinforcing defensive layers and controls across the systems and networks the regulation covers |
| nrc-cyber-rg-5-71 | ch05-cyber-security-versus-sdoe-contrast.md | Cyber program versus RG 1.152 SDOE contrast from carried nrc-nuclear fence facts; which side of the fence a question belongs to |
| nrc-cyber-rg-5-71 | ch06-program-lifecycle-and-periodic-review.md | Program lifecycle elements: establish, implement, monitor, sustain, and reassess; change concerns named without tactic detail |
| nrc-cyber-rg-5-71 | glossary.md (support file) | Cyber security program terms this pack uses, keyed to the RG 5.71 Rev. 1 and 73.54 orientation chapters |
| nrc-cyber-rg-5-71 | cheatsheet.md (support file) | Which chapter owns the cyber program question, the pin rules, and the sensitive-content limits |

## 7. Accident Monitoring

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nrc-accident-monitoring-rg-1-97 | ch01-rg-1-97-role-and-scope.md | RG 1.97 Rev. 5 role and scope: accident monitoring instrumentation criteria, oriented as control-room operator information during and after accidents |
| nrc-accident-monitoring-rg-1-97 | ch02-revision-history-and-the-rev-5-pin.md | Revision history at pin level: Rev. 5 current (ML18136A762), DG-1335 issued as final Rev. 5, Rev. 4 predecessor, older Type and Category schemes |
| nrc-accident-monitoring-rg-1-97 | ch03-variables-and-selection-criteria.md | The guide frames which variables are monitored and selection criteria; severe-accident-management-guideline variables named as a Rev. 5 addition; variable lists named out |
| nrc-accident-monitoring-rg-1-97 | ch04-categorization-and-design-criteria.md | Design criteria and categorization of monitored variables at framework level; category labels and design detail live in the guide; no how-to |
| nrc-accident-monitoring-rg-1-97 | ch05-ieee-497-2016-endorsement-hook.md | Rev. 5 endorsement of IEEE Std 497-2016 with exceptions and clarifications; the standard is named only and its text is not packaged |
| nrc-accident-monitoring-rg-1-97 | ch06-applicability-and-licensing-basis.md | Applicability orientation: technology-neutral, Part 52 language, and the governing revision read from the plant licensing record |
| nrc-accident-monitoring-rg-1-97 | glossary.md (support file) | Accident monitoring terms this pack uses, keyed to the RG 1.97 Rev. 5 orientation chapters |
| nrc-accident-monitoring-rg-1-97 | cheatsheet.md (support file) | Which chapter owns the accident monitoring question, the pin rule, and the named-only limits |
