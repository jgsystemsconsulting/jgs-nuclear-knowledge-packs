<!--
Copyright (c) 2026 JG Systems Consulting Ltd.: MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/).

## [Unreleased]

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
