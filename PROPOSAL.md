# Proposal: vital-info-translations

**Proposer:** jdev1977 (drafted by Claude Code)
**Date:** 2026-06-28
**Domain(s):** translation, public-health, public-safety
**Lane:** donated
**Requestor / beneficiary:** community health workers & NGOs in low-resource-language regions  ·  **Verified need:** yes (to be confirmed per partner)

## Summary
Translate vetted, life-critical public-health and safety guidance (first aid, maternal/child
health, vaccine info, disaster preparedness, water/sanitation) into low-resource languages.
Extends the existing `health-info-translations` pilot from a single factsheet to a standing,
multi-source, multi-language program.

## Why it qualifies as a good deed
- **Tangible public benefit:** accurate health guidance in a reader's own language saves lives.
- **Freely available:** all translations open-access under a license compatible with the source.
- **Not primarily for-profit:** outputs go to NGOs/health workers and the public.
- **No harm/misinformation:** medical accuracy is reviewed; sources are vetted (WHO, MoH, MSF, etc.).
- **Executable by AI sessions:** drafting decomposes per document × language; human review gates it.

## Scope / first tasks
- (small) Build the source allow-list with per-source license terms (WHO, national MoH, CDC, MSF).
- (medium) Translate one WHO/MoH factsheet into one target language + reviewer checklist.
- (small) Glossary of preserved medical terminology per language pair.
- (medium) Reviewer-handoff template (qualified reviewer sign-off recorded in the PR).

## Definition of shipped
A reviewed translation set, correctly licensed and attributed, delivered to and adopted by the
requesting NGO/health authority for distribution.

## Risks / review needs
**Risk tier: medium.** Requires a qualified language reviewer with health-translation competence.
**License gate:** each source's reuse terms must be verified and honored — never relicense
copyrighted source material (e.g., WHO content carries WHO terms + a required translation
disclaimer; it is *not* CC-BY). Record provenance and the required attribution in every deliverable.
