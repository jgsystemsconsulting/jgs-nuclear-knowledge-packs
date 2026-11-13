<!--
Copyright (c) 2026 JG Systems Consulting Ltd.: MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/).

## [Unreleased]
- Add `nrc-hsi-nureg-0700`: orientation notes on human-system interface design review, synthesized NRC NUREG-0700 Revision 4, January 2026, ML26022A094, verified via official NRC publication page; synthesized HSI design review orientation, no guideline items or numeric design values packaged; registration surfaces refreshed including EXPECTED_NOTES_COUNT 119 to 128 and new Human Factors and HSI cluster; pre-1.0, no version bump.

- Add `nrc-fire-rg-1-189`: orientation notes on fire protection program for nuclear power plants, synthesized from NRC RG 1.189 Rev 5, October 2023, ML23214A287 (Federal Register notice 88 FR 76989). Program orientation only; NFPA 805 and NFPA 804 named only signpost designations, no numeric design values packaged. Registration surfaces refreshed: EXPECTED_NOTES_COUNT moves 110 to 119 with new Fire Protection Programs cluster (9 entries); H-02 folded into signpost (NFPA 804 row added beside NFPA 805). Release version stays 0.3.0.

- Add `nrc-non-lwr-ticap-rg-1-233`: orientation notes on technology-inclusive risk-informed performance-based non-LWR licensing basis methodology, synthesized NRC RG 1.233 Rev 0, June 2020, ML20091L698 (Federal Register notice 85 FR 35339). NEI 18-04 named only, never reproduced; methodology stages at outline depth only; Part 50, Part 52, RG 1.232, RG 1.174, RG 1.200, and Part 53 named only. Registration surfaces refreshed: EXPECTED_NOTES_COUNT moves 101 to 110; Regulatory Framework and Staff Review cluster moves 43 to 52. Release version stays 0.3.0.
- Add `nrc-non-lwr-pdc-rg-1-232`: orientation notes on developing principal design criteria for non-light water reactors, synthesized from NRC RG 1.232 Rev 0, April 2018, ML17325A611 (Federal Register notice 83 FR 15178). Appendix families at family level only and no criterion text; functional containment and mechanistic source term as orientation concepts; Part 50, Part 52, RG 1.233, and Part 53 named only. EXPECTED_NOTES_COUNT moves 92 to 101. Release version stays 0.3.0.
- Add `nrc-app-b-criteria`: criterion lookup notes on the eighteen quality assurance criteria of 10 CFR Part 50 Appendix B, synthesized from eCFR public-domain text (title 10 current as of 2026-11-09; pin-check 2026-11-11). Criterion lookup only, not a QA program; RG 1.28 named only and NQA-1 text not packaged. EXPECTED_NOTES_COUNT moves from 76 to 84. Release version stays 0.3.0.
- Add `nrc-pra-adequacy-rg-1-200`: orientation notes on PRA technical adequacy, synthesized from NRC RG 1.200 Rev. 3, December 2020, ML20238B871 (listing-page pin 2026-11-08; build re-check 2026-11-11). Adequacy orientation only; ASME/ANS RA-Sa-2009 named by designation and endorsement fact only, NUREG-1855 and SRP Chapter 19 named only. EXPECTED_NOTES_COUNT moves 84 to 92. Release version stays 0.3.0.
- Add `nrc-10cfr-part52-col`: orientation notes on 10 CFR Part 52 licensing actions (early site permits, design certifications, combined licenses and ITAAC, manufacturing licenses), synthesized from eCFR public-domain text (title 10 current as of 2026-11-09; pin-check 2026-11-11), paired with RG 1.206 Rev 1 pin orientation (October 2018, ML18131A181; Federal Register notice 2018-22262; guide PDF body not captured). Selected slices only; design-specific appendix rules, Part 53, and non-LWR principal design criteria named only. EXPECTED_NOTES_COUNT moves from 67 to 76. Release version stays 0.3.0.
- Add `nrc-accident-monitoring-rg-1-97`: orientation notes on accident monitoring instrumentation criteria, synthesized from NRC RG 1.97 Rev. 5, May 2019, ML18136A762 (Federal Register notice 2019-08819; dual-source pin 2026-11-09). No HSI guidance, no instrumentation design how-to, and no variable lists or design detail; IEEE Std 497-2016 and NUREG-0700 are named only. EXPECTED_NOTES_COUNT moves from 58 to 67. Release version stays 0.3.0.
- Add `nrc-cyber-rg-5-71`: orientation notes on cyber security programs for nuclear power reactors, synthesized from NRC RG 5.71 Rev. 1, February 2023, ML22258A204, and 10 CFR 73.54 public eCFR slices (pin-check 2026-11-09; section unchanged since 2017-01-01). No security-control implementation guidance and no tactic detail; G-02 and G-03 are named only. EXPECTED_NOTES_COUNT moves from 49 to 58. Release version stays 0.3.0.
- Add `nrc-risk-informed-rg-1-174`: orientation notes on risk-informed decisions on plant-specific changes to the licensing basis, synthesized from NRC RG 1.174 Rev. 3, 2018, ML17317A256. The guide's numeric guideline tables are named as living in the guide and are not reproduced; RG 1.200 Rev 3 and NUREG-1855 are named only. EXPECTED_NOTES_COUNT moves from 40 to 49. Release version stays 0.3.0.
- Add `nrc-qa-rg-1-28`: orientation notes on quality assurance program criteria for design and construction, synthesized from NRC RG 1.28 Rev 6, September 2023, ML23177A002 (Federal Register notice 2023-19548). Rev 6 endorses ASME NQA-1-2017, NQA-1-2019, and NQA-1-2022 Part I and Part II requirements with clarifications and regulatory positions, plus NEI 14-05A Rev 1; NQA-1 text is named only, never reproduced. EXPECTED_NOTES_COUNT moves from 31 to 40. Release version stays 0.3.0.
- Add `nrc-10cfr-part50-licensing-basis`: orientation notes on the 10 CFR Part 50 licensing basis, synthesized from eCFR public-domain text (title 10 current as of 2026-11-05; pin-check 2026-11-08). Selected slices: 50.2 definitions, 50.34, 50.36, 50.54, 50.59, Appendix A index, Appendix B pointer. EXPECTED_NOTES_COUNT moves from 22 to 31. Release version stays 0.3.0.
- Add `nrc-btp-7-18-plc`: orientation notes for PLCs in digital safety I&C, pinned to NUREG-0800 BTP 7-18 Rev. 6, August 2016, ML16019A327. PDF body was not captured. EXPECTED_NOTES_COUNT moves from 12 to 22. Release version stays 0.3.0.

## [0.3.0]

### Added

- nrc-nuclear gains two sources and two chapters. Regulatory Guide 1.152 Rev 4 (July 2023, ML23054A463) is ch09 (criteria for programmable digital devices and the secure development and operational environment). NUREG-0800 Appendix 7.1-D Rev 1 (August 2016, ML16019A114) is ch10 (staff evaluation of the application of IEEE Std 7-4.3.2). Chapter 08 now points at ch09 and ch10. EXPECTED_NOTES_COUNT moves from 10 to 12. Regulatory Framework floor moves from 5 to 7. BTP 7-19 remains outside the pack.

## [0.2.0]

### Added

- nuclear-signpost pack (kind: signpost): IEEE Std 603-1991, 7-4.3.2-2003, 828-2005, 829-2008, 830-1998, 1008-1987, 1012-2004, 1028-2008, 1074-2006; IEC 60880 ed. 2.0:2006, IEC 61513 ed. 2.0:2011, IEC 62138 ed. 2.0:2018; IAEA SSG-39 designation-only. Pointers only; free path pack: nrc-nuclear.
- Catalogue flip: 1 pack · 1 signpost; expected_signposts ["nuclear-signpost"].

## [0.1.0]: 2026-09-24

### Added

- Initial public release: nrc-nuclear knowledge pack (7 NRC sources: Regulatory Guide 1.168 Rev 2, Regulatory Guides 1.169-1.173 Rev 1, NUREG-0800 BTP 7-14 Rev 6) and /nuclear orchestrator.
