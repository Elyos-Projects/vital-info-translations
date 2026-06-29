# Source allow-list — `vital-info-translations`

This directory holds the **per-source license allow-list** that gates every translation in
`vital-info-translations`. Source material for this project is **not uniformly CC-BY** — WHO
content carries WHO terms (CC BY-NC-SA 3.0 IGO) plus a **mandatory translation disclaimer**, MoH
terms vary, and CDC is usually U.S. public domain but can embed third-party material. **Nothing may
be translated until its source is allow-listed here with verified terms.**

## Files

| File | Purpose |
|---|---|
| `allow-list.yaml` | The allow-list itself: one entry per source, with license terms, attribution, disclaimer, and verification status. |
| `allow-list.schema.json` | JSON Schema (draft-07) the YAML must conform to. The canonical project schemas live in the external Elyos `packages/schema` package (`allowListSchema`); this file is the concrete, in-repo copy used for structural CI here. |
| `validate.py` | Stand-alone structural check (PyYAML + stdlib) that validates `allow-list.yaml` against the schema **and** the task's acceptance criteria. This is the `tooling-001` structural gate for this repo. |

## ⚠️ Status of the current entries (read this first)

**Every entry in `allow-list.yaml` is currently `reviewStatus: provisional` and NOT cleared for
translation.** The entries were drafted by an automated agent in the donated lane **without live web
access in this run**. That means:

- The `snapshot.text` values are good-faith **reproductions of well-known, publicly-documented
  standard terms** (CC BY-NC-SA 3.0 IGO, the WHO translation disclaimer, the Open Government
  Licence v3.0, 17 U.S.C. §105) — **not** bytes captured from the live source pages.
- `snapshot.sha256`, `snapshot.archiveUrl`, and per-entry `retrievalDate` are **`null`** because no
  live fetch/capture was performed. `capturedFromLiveFetch` is `false` everywhere.
- `verifiedBy` records the **automated desk review only**; no qualified human license/compliance
  reviewer has signed off yet.

This is deliberate and honest: per `PLAN.md`, human confirmation + a captured license snapshot is a
**blocking prerequisite** before any translation. Do **not** treat these snapshots as the
authoritative license. The **original source edition is always the binding edition.**

## The hard gate

> A source may be used for translation **only when** `status == "included"` **AND**
> `reviewStatus == "confirmed"`.

`license-002` (the per-deliverable license gate) additionally cross-checks each translation's
attribution + disclaimer + output license against the matching `included`/`confirmed` source entry.

## Schema (per-source entry)

Top-level: `schemaVersion`, `generatedDate`, `fileLicense` (this file is **MIT** as project
tooling/data — that does **not** relicense any source content), `verificationPolicy`, and
`sources[]`. Each source entry records:

| Field | Meaning |
|---|---|
| `id` | Stable kebab-case identifier. |
| `name`, `publisher` | Human-readable source and rights-holder. |
| `status` | `included` (approved, subject to `reviewStatus`) or `excluded`. |
| `reviewStatus` | `provisional` (drafted, not yet human-confirmed) or `confirmed` (human-signed-off, snapshot captured). |
| `canonicalUrl` | Canonical URL of the source/license. |
| `documentScope` | What the entry covers and what it excludes (e.g. third-party material). |
| `sourceVersion` | Version/date of the source document or policy. |
| `retrievalDate` | Date the page was **actually** live-fetched (`null` until done). |
| `license.name` / `license.url` | License name and URL. |
| `license.isCcBy` | **`true` only for genuine CC BY.** WHO is `false`. |
| `license.derivativesAllowed` / `translationAllowed` / `commercialUseAllowed` | `yes` / `no` / `conditional` / `unknown`. |
| `license.snapshot.text` | Reproduction of the relevant license/reuse terms. |
| `license.snapshot.capturedFromLiveFetch` | `true` only if `text` came from a live retrieval. |
| `license.snapshot.sha256` / `archiveUrl` | SHA-256 of captured bytes + web-archive (Wayback) URL (`null` until captured). |
| `license.snapshot.integrityNote` | What still needs capturing. |
| `requiredAttribution` | Exact attribution string a deliverable must carry. |
| `requiresDisclaimer` / `disclaimerText` | Whether a disclaimer is mandatory and its verbatim text. |
| `outputLicense` | License a **derived translation** must carry (source-compatible). |
| `exclusionReason` | Why a source is `excluded` (required when excluded). |
| `verifiedBy` / `verifiedDate` / `verificationMethod` | Who/when/how the entry was checked. |
| `notes` | Free-text caveats. |

## Verification process — promoting `provisional` → `confirmed`

A qualified human **license/compliance reviewer** (initially the acting maintainer, per `PLAN.md`)
must, **before** the source is translated:

1. **Live-fetch** the `canonicalUrl` and `license.url`.
2. **Capture** the license (and the specific source document) bytes; set `snapshot.text` to the
   captured terms, set `capturedFromLiveFetch: true`, record `snapshot.sha256` (SHA-256 of the
   captured bytes) and a `snapshot.archiveUrl` (Wayback or equivalent), and set `retrievalDate`.
3. **Confirm derivatives/translation are permitted** for the specific document, and set the
   `derivativesAllowed` / `translationAllowed` / `commercialUseAllowed` flags accordingly.
4. **Confirm the exact required disclaimer wording verbatim** (e.g. the WHO translation disclaimer)
   and the `requiredAttribution` string, and the source-compatible `outputLicense`.
5. Set `verifiedBy` (the reviewer), `verifiedDate`, `verificationMethod`, and only then
   `reviewStatus: confirmed`.

If derivatives/translation permission **cannot** be established, or terms are unclear or
incompatible, the source is set `status: excluded` with an `exclusionReason` — **do not translate**
("if unclear, don't translate"). A **source-change watcher** (M0 manual, M1 automated) re-fetches
confirmed sources, recomputes `sha256`, and flags drift for re-verification.

## WHO — special handling (do not skip)

WHO content is **NOT CC-BY**. The default WHO license is **CC BY-NC-SA 3.0 IGO** (NonCommercial +
ShareAlike), and **every WHO translation must carry the mandatory WHO translation disclaimer**:

> "This translation was not created by the World Health Organization (WHO). WHO is not responsible
> for the content or accuracy of this translation. The original English edition shall be the binding
> and authentic edition."

Terms vary per publication — confirm the exact license and disclaimer **on each specific WHO
document**. A WHO-sourced translation inherits **BY-NC-SA-style** terms; it may **not** be
relicensed more permissively (e.g. as CC BY).

## Adding or excluding a source

- **Add:** append a new entry with a unique `id`, fill every required field, then run the
  verification process above to reach `confirmed`. Start at `provisional`.
- **Exclude:** set `status: excluded` and a clear `exclusionReason` (e.g. all-rights-reserved, no
  translation permission). Excluded sources are never translated until revised with granted terms.

## Validating

```bash
# Requires PyYAML (pip install pyyaml)
python sources/validate.py
```

The script checks schema conformance and the acceptance criteria (≥ 3 sources; ≥ 1 WHO and ≥ 1
included MoH/CDC; WHO marked NOT CC-BY with a mandatory disclaimer; every entry has
`verifiedBy`/`verifiedDate`; every excluded source has a reason). Wire it into `pnpm test` / CI so a
malformed or non-conformant allow-list fails the build.

## Licensing of this directory

These metadata/tooling files (`allow-list.yaml`, `allow-list.schema.json`, `validate.py`,
`README.md`) are released under the project's **MIT** license. **This does not relicense any source
content.** Translated content always follows its source's terms (see `outputLicense` per entry).
