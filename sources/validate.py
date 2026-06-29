#!/usr/bin/env python3
"""Structural validator for sources/allow-list.yaml.

Mirrors the structural CI check (`tooling-001` in PLAN.md) for this repo, where
the canonical JSON Schemas live in the external Elyos schema package
(`packages/schema/src/schemas.ts`). This stand-alone script lets the allow-list
be validated in CI here using only PyYAML + the Python standard library, against
./allow-list.schema.json plus the task's acceptance criteria.

Usage:
    python sources/validate.py
Exit code 0 = OK, 1 = validation failure, 2 = environment problem (no PyYAML).
"""
import json
import re
import sys
import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
YAML_PATH = HERE / "allow-list.yaml"
SCHEMA_PATH = HERE / "allow-list.schema.json"

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"environment error: PyYAML not installed ({exc})")
    sys.exit(2)


def is_date(value: str) -> bool:
    if not isinstance(value, str) or not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
        return False
    try:
        datetime.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def main() -> int:
    data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []

    for key in schema["required"]:
        if key not in data:
            errors.append(f"top-level missing field: {key}")

    sources = data.get("sources", []) or []
    if len(sources) < 3:
        errors.append("acceptance: need >= 3 sources")

    src_required = schema["definitions"]["source"]["required"]
    lic_required = schema["definitions"]["license"]["required"]
    snap_required = schema["definitions"]["snapshot"]["required"]
    yes_no = {"yes", "no", "conditional", "unknown"}

    who_seen = False
    included_moh_or_cdc = False
    excluded_with_reason = 0

    for src in sources:
        sid = src.get("id", "?")
        for key in src_required:
            if key not in src:
                errors.append(f"[{sid}] missing field: {key}")
        if src.get("status") not in {"included", "excluded"}:
            errors.append(f"[{sid}] bad status: {src.get('status')!r}")
        if src.get("reviewStatus") not in {"provisional", "confirmed"}:
            errors.append(f"[{sid}] bad reviewStatus: {src.get('reviewStatus')!r}")
        if not src.get("verifiedBy"):
            errors.append(f"[{sid}] empty verifiedBy")
        if not is_date(src.get("verifiedDate", "")):
            errors.append(f"[{sid}] verifiedDate not an ISO date")
        if not isinstance(src.get("requiresDisclaimer"), bool):
            errors.append(f"[{sid}] requiresDisclaimer not boolean")

        lic = src.get("license", {}) or {}
        for key in lic_required:
            if key not in lic:
                errors.append(f"[{sid}] license missing: {key}")
        for field in ("derivativesAllowed", "translationAllowed", "commercialUseAllowed"):
            if lic.get(field) not in yes_no:
                errors.append(f"[{sid}] license.{field} not in {sorted(yes_no)}")
        if not isinstance(lic.get("isCcBy"), bool):
            errors.append(f"[{sid}] license.isCcBy not boolean")
        snap = lic.get("snapshot", {}) or {}
        for key in snap_required:
            if key not in snap:
                errors.append(f"[{sid}] snapshot missing: {key}")
        if not isinstance(snap.get("capturedFromLiveFetch"), bool):
            errors.append(f"[{sid}] snapshot.capturedFromLiveFetch not boolean")

        # Acceptance criteria specifics
        if "who" in sid:
            who_seen = True
            if lic.get("isCcBy") is not False:
                errors.append(f"[{sid}] WHO entry must record isCcBy = false (NOT CC-BY)")
            if not src.get("requiresDisclaimer"):
                errors.append(f"[{sid}] WHO entry must set requiresDisclaimer = true")
            if not src.get("disclaimerText"):
                errors.append(f"[{sid}] WHO entry must carry the mandatory disclaimerText")
        if src.get("status") == "included" and ("cdc" in sid or "moh" in sid):
            included_moh_or_cdc = True
        if src.get("status") == "excluded":
            if src.get("exclusionReason"):
                excluded_with_reason += 1
            else:
                errors.append(f"[{sid}] excluded but missing exclusionReason")
        if src.get("status") == "included":
            if not src.get("requiredAttribution"):
                errors.append(f"[{sid}] included but missing requiredAttribution")
            if not src.get("outputLicense"):
                errors.append(f"[{sid}] included but missing outputLicense")

    if not who_seen:
        errors.append("acceptance: no WHO source present")
    if not included_moh_or_cdc:
        errors.append("acceptance: no included MoH/CDC source present")
    if excluded_with_reason < 1:
        errors.append("acceptance: no excluded-with-reason source present")

    print(
        f"sources={len(sources)} who={who_seen} moh_or_cdc={included_moh_or_cdc} "
        f"excluded_with_reason={excluded_with_reason}"
    )
    if errors:
        print("VALIDATION FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("VALIDATION OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
