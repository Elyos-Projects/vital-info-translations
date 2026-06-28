# TASKS — vital-info-translations

> Status: Draft · Version: 0.1.0 · Last updated: 2026-06-28 · Owner: TBD (maintainer) · Lane: donated

The backlog for the `vital-info-translations` good-deed project. Read alongside
[PLAN.md](./PLAN.md). Milestones (M0–M3) match the roadmap there.

## How these tasks map to Elyos

Each task below becomes an **Elyos Task JSON** validated against
`packages/schema/src/schemas.ts`. Field mapping:

- **id** — stable slug id, e.g. `vital-info-translations-sources-001` (table column `ID`).
- **title** — the task title.
- **project** — always `vital-info-translations`.
- **type** — one of `code | research | writing | data | design-spec | maintenance` (table `Type`).
- **lane** — `donated` for all current tasks (no funded/API execution). Funded tasks would need
  `fundedBudgetUsd`; none here.
- **priority** — `high | medium | low`.
- **domain** — array, e.g. `["translation","public-health"]`.
- **riskTier** — `low | medium | high`. Translation/glossary/review tasks are **medium** (need a
  qualified reviewer); pure tooling/process tasks are **low** (table `Risk`).
- **urgent** — boolean (default false; no live emergency yet).
- **deliverable** — `pr | dataset | document | translation` (table `Deliverable`).
- **tokenEstimate** — `small | medium | large` (table `Size`).
- **status** — `open | in-progress | review | delivered | done` (all start `open`).
- **context / objective** — why + what.
- **acceptanceCriteria[]** — checkable bullets (listed below tables for key tasks).
- **resources[]** — links/paths (allow-list, glossary, source URLs, templates).
- **output** — path/description of the produced artifact.
- **requestor** — partner/requestor; `TO BE SECURED` until a partner is confirmed.
- **verifiedNeed** — boolean; **`false`** wherever value depends on an unsecured partner.
- **outputLicense** — MIT for code/tooling; **source-compatible license + required disclaimer**
  for translated content (e.g., WHO → CC BY-NC-SA 3.0 IGO + WHO translation disclaimer, **never**
  CC-BY).

---

## Milestone M0 — Foundation & cold-start (no partner required)

Goal: stand up license/glossary/review machinery and prove the pipeline on one factsheet into one
language, end-to-end except final partner adoption.

| ID | Title | Type | Size | Risk | Deliverable | Depends on | Reviewer |
|---|---|---|---|---|---|---|---|
| vital-info-translations-sources-001 | Build source allow-list with per-source license terms | data | small | low | dataset | — | Maintainer / License reviewer |
| vital-info-translations-review-001 | Reviewer checklist for health translations | writing | small | low | document | — | Maintainer |
| vital-info-translations-review-002 | Reviewer-handoff template (sign-off recorded in PR) | writing | small | low | document | review-001 | Maintainer |
| vital-info-translations-glossary-001 | Glossary of preserved medical terminology (1 language pair) | data | small | medium | dataset | sources-001 | Qualified reviewer |
| vital-info-translations-license-001 | Per-deliverable license & attribution check procedure | research | small | low | document | sources-001 | License reviewer |
| vital-info-translations-translate-001 | Translate one WHO/MoH factsheet into one target language | translation | medium | medium | translation | sources-001, glossary-001, review-001 | Qualified reviewer |
| vital-info-translations-tooling-001 | Metadata schema + CI structural check for source/provenance files | code | small | low | pr | sources-001 | Maintainer |

**Acceptance criteria — key M0 tasks**

`sources-001` (allow-list)
- Allow-list file (`sources/allow-list.yaml`) lists ≥ 3 sources (incl. at least one WHO and one
  MoH/CDC) with: name, canonical URL, version/date, retrieval date, license name + URL, **snapshot
  of license text**, derivatives-allowed flag, required attribution string, and required
  disclaimer text (where applicable).
- WHO entries explicitly record the **mandatory translation disclaimer** and that terms are **not**
  CC-BY.
- Each entry has `verifiedBy` + `verifiedDate`; any source with unclear/incompatible terms is
  marked **excluded** with a reason.

`translate-001` (first factsheet)
- One allow-listed WHO/MoH factsheet translated in full into one target language, UTF-8 Markdown.
- Dosages, units, and **negations** preserved exactly; preserved terms follow `glossary-001`.
- Ships `provenance.yaml` (source id, version, retrieval date, glossary version, translator,
  reviewer) and `attribution.txt` (attribution + required disclaimer verbatim).
- **Qualified reviewer sign-off recorded in the PR**; reviewer checklist completed.
- License check (`license-001`) passed; output license is **source-compatible**, not a relicense.

`glossary-001` (terminology)
- ≥ 30 source→target term entries covering medical terms, units, and "preserve verbatim" items,
  with notes/transliteration rules; reviewed by a qualified reviewer for the pair.

`license-001` (license check procedure)
- A checkable procedure that, for any deliverable, verifies: source is allow-listed, output
  license is compatible, attribution present, mandatory disclaimer present and verbatim, provenance
  complete. Documented as a checklist tooling can later enforce.

**M0 Definition of Done:** allow-list (≥3 verified sources) + checklist + handoff template + 1
glossary + license-check procedure merged; **one factsheet translated into one language with
qualified reviewer sign-off and a passing license/attribution check**; CI structural checks green.
Partner adoption deferred to M2 (so M0 deliverables carry `verifiedNeed: false`).

---

## Milestone M1 — Repeatability & reviewer network

Goal: make the pipeline repeatable and recruit/qualify reviewers.

| ID | Title | Type | Size | Risk | Deliverable | Depends on | Reviewer |
|---|---|---|---|---|---|---|---|
| vital-info-translations-reviewers-001 | Reviewer qualification criteria + onboarding doc | writing | small | low | document | review-001 | Maintainer |
| vital-info-translations-reviewers-002 | Recruit/engage ≥2 qualified reviewers or a translation NGO | research | medium | low | document | reviewers-001 | Maintainer / Steward |
| vital-info-translations-glossary-002 | Extend glossary to a second language pair | data | small | medium | dataset | glossary-001 | Qualified reviewer |
| vital-info-translations-license-002 | License-check tooling (lint allow-list + deliverable metadata) | code | medium | low | pr | license-001, tooling-001 | Maintainer |
| vital-info-translations-translate-002 | Translate a second factsheet (different topic) | translation | medium | medium | translation | translate-001 | Qualified reviewer |
| vital-info-translations-process-001 | Document end-to-end pipeline runbook | writing | small | low | document | translate-001, license-001 | Maintainer |

**Acceptance criteria — key M1 tasks**

`reviewers-001`
- Written, objective criteria for "qualified language reviewer with health-translation competence"
  (native/near-native target language, health-translation experience, conflict-of-interest
  declaration), plus an onboarding/sign-off workflow.

`license-002`
- Tooling validates each deliverable's metadata against its allow-list source entry and **fails**
  if attribution or required disclaimer is missing, or if output license is incompatible with the
  source; runs in CI.

**M1 Definition of Done:** qualification criteria published and ≥ 2 qualified reviewers (or a
translation-NGO partner) engaged; glossary covers ≥ 2 language pairs; license check enforced in CI;
a second reviewed factsheet completed; pipeline runbook merged.

---

## Milestone M2 — First partner delivery (needs partner)

Goal: deliver an adopted translation set. **All tasks gated on a secured partner**
(`verifiedNeed` flips to `true` only when the partner is confirmed).

| ID | Title | Type | Size | Risk | Deliverable | Depends on | Reviewer |
|---|---|---|---|---|---|---|---|
| vital-info-translations-partner-001 | Secure first partner; agree languages + priority docs | research | medium | low | document | reviewers-002 | Steward / Maintainer |
| vital-info-translations-translate-003 | Translate partner-priority document set into agreed language | translation | large | medium | translation | partner-001, glossary-002 | Qualified reviewer |
| vital-info-translations-delivery-001 | Package + deliver set; confirm partner adoption | writing | small | medium | document | translate-003, license-002 | Steward |

**Acceptance criteria — key M2 tasks**

`partner-001`
- A named NGO/health authority confirmed in writing as requestor; agreed target language(s) and a
  prioritized document list; reviewer coverage for the language confirmed. On completion, related
  tasks update `requestor` and `verifiedNeed: true`.

`delivery-001`
- Delivered set includes translation(s), provenance, attribution + disclaimer, reviewer sign-off;
  license check green; **partner confirms adoption for distribution in writing** (recorded in the
  PR/receipt). This is the first true **Definition of Shipped** event.

**M2 Definition of Done:** partner secured (`verifiedNeed=true`); ≥ 1 reviewed, correctly-licensed
translation set **delivered and confirmed adopted** by the partner.

---

## Milestone M3 — Scale program

Goal: scale to multiple documents/languages with sustained quality and tracked outcomes.

| ID | Title | Type | Size | Risk | Deliverable | Depends on | Reviewer |
|---|---|---|---|---|---|---|---|
| vital-info-translations-scale-001 | Translate additional documents across ≥2 languages | translation | large | medium | translation | delivery-001 | Qualified reviewers |
| vital-info-translations-rotation-001 | Establish reviewer rotation + load balancing | maintenance | small | low | document | reviewers-002 | Maintainer |
| vital-info-translations-outcomes-001 | Outcome tracking: post-delivery defect + feedback log | data | small | low | dataset | delivery-001 | Steward |
| vital-info-translations-maint-001 | Source re-verification + glossary maintenance cadence | maintenance | small | low | document | sources-001 | Maintainer |

**Acceptance criteria — key M3 tasks**

`outcomes-001`
- A maintained log capturing, per delivered set: adoption status, post-delivery critical defects
  (target 0), and partner usefulness feedback; feeds PLAN.md success metrics.

`maint-001`
- A documented cadence to re-verify allow-list sources (detect upstream/license changes via the
  stored snapshot) and refresh glossaries; defines withdrawal procedure if a license changes to
  forbid reuse.

**M3 Definition of Done:** ≥ 3 documents across ≥ 2 languages adopted; reviewer rotation operating;
outcome tracking live; source/glossary maintenance cadence in effect; named sustainability owner.

---

## Backlog / future

Sized but unscheduled:

- **(medium) Print/complex-script delivery formats** — partner-driven layout/typesetting for
  scripts beyond plain Markdown.
- **(medium) Migrate `health-info-translations` pilot** factsheet + glossary into this program.
- **(small) Source-change watcher** — periodic diff of allow-listed source URLs vs. stored
  snapshots to flag updates/retractions.
- **(medium) Back-translation QA pass** — independent back-translation as an extra accuracy gate
  for the highest-stakes documents.
- **(small) Pivot-language attribution bundle** — bilingual attribution/disclaimer packaging where
  partners require both target + pivot language.
- **(large, funded — needs escrow) Surge drafting under funded lane** — metered drafting against a
  hard per-task budget for high-demand events; would require `fundedBudgetUsd` and remains out of
  scope for v0.1.

---

## Example task JSON

Schema-valid Task JSON for the first M0 task. `verifiedNeed` is **false** (no partner secured);
`outputLicense` is MIT because the allow-list dataset is project metadata, not translated source
content.

```json
{
  "id": "vital-info-translations-sources-001",
  "title": "Build source allow-list with per-source license terms",
  "project": "vital-info-translations",
  "type": "data",
  "lane": "donated",
  "priority": "high",
  "domain": ["translation", "public-health", "public-safety", "licensing"],
  "riskTier": "low",
  "urgent": false,
  "deliverable": "dataset",
  "tokenEstimate": "small",
  "status": "open",
  "context": "vital-info-translations translates vetted public-health/safety guidance into low-resource languages. Source material is NOT uniformly CC-BY: WHO content carries WHO terms (often CC BY-NC-SA 3.0 IGO) plus a mandatory translation disclaimer, MoH terms vary, CDC is often US public domain but may embed third-party material. Nothing may be translated until its source is allow-listed with verified terms.",
  "objective": "Create a structured, per-source allow-list recording each approved source's license terms, derivatives permission, required attribution, and any mandatory disclaimer, so the per-deliverable license gate can be checked consistently.",
  "acceptanceCriteria": [
    "sources/allow-list.yaml lists >= 3 sources including at least one WHO and one MoH or CDC source",
    "Each entry records: name, canonical URL, version/date, retrieval date, license name + URL, snapshot of license text, derivatives-allowed flag, required attribution string, required disclaimer text",
    "WHO entries explicitly capture the mandatory translation disclaimer and note the terms are NOT CC-BY",
    "Each entry has verifiedBy and verifiedDate; any source with unclear or incompatible terms is marked excluded with a reason",
    "File validates against the project metadata schema and passes CI structural checks"
  ],
  "resources": [
    "C:/code/elyos/governance/proposals/vital-info-translations.md",
    "C:/code/elyos/planning/projects/vital-info-translations/PLAN.md",
    "WHO permissions/licensing and translation policy pages",
    "CDC content-use / public-domain notice"
  ],
  "output": "sources/allow-list.yaml plus a short README documenting the allow-list schema and verification process",
  "requestor": "TO BE SECURED",
  "verifiedNeed": false,
  "outputLicense": "MIT"
}
```
