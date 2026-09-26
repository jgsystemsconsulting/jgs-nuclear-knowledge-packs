# Capability to Knowledge-Pack Map

Working artifact mapping sector technical capabilities to the pack chapters that provide
reference depth for each capability. Empty-tree template seed: no content packs yet.

Rules of construction:
- Every chapter in every pack under `packs/<slug>/chapters/` is assigned to exactly one capability cluster (best fit).
- Signpost packs contain no chapters and are not mapped.
- Machine-readable version: `docs/capability-pack-map.json`.
- Machine-readable classification rules: `docs/classification-rules.json`.
- Changelog (v0.1.0): empty-tree template seed.

## Summary

| Cluster | Entries |
|---|---|
| 1. Life Cycle & Requirements | 3 |
| 2. Verification & Testing | 2 |
| 3. Regulatory Framework & Staff Review | 5 |
| **Total** | **10** |

## 1. Life Cycle & Requirements

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nrc-nuclear | ch02-software-life-cycle-processes.md | RG 1.173 Rev 1 software life cycle processes and BTP 7-14 plan-level review of life cycle plans |
| nrc-nuclear | ch03-software-requirements-specifications.md | RG 1.172 Rev 1 software requirements specifications for software and complex electronics |
| nrc-nuclear | ch04-software-configuration-management-plans.md | RG 1.169 Rev 1 software configuration management plans and the BTP 7-14 CM plan review |

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
| nrc-nuclear | glossary.md (support file) | Software assurance terms used across the nrc-nuclear chapters |
| nrc-nuclear | cheatsheet.md (support file) | Decision rules routing software assurance questions to the right nrc-nuclear chapter |
