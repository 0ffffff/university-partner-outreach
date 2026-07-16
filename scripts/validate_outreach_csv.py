#!/usr/bin/env python3
"""Validate outreach CSV schema and basic row hygiene.

Does not verify that mailboxes exist or that people currently work at the company.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REQUIRED = ["First Name", "Last Name", "Title", "Company Name", "Email"]
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            return ["Missing header row"]
        headers = [h.strip() for h in reader.fieldnames]
        for col in REQUIRED:
            if col not in headers:
                errors.append(f"Missing required column: {col}")
        if errors:
            return errors

        seen_names: set[tuple[str, str]] = set()
        seen_emails: set[str] = set()
        for i, row in enumerate(reader, start=2):
            first = (row.get("First Name") or "").strip()
            last = (row.get("Last Name") or "").strip()
            title = (row.get("Title") or "").strip()
            company = (row.get("Company Name") or "").strip()
            email = (row.get("Email") or "").strip()

            if not first:
                errors.append(f"L{i}: empty First Name")
            if not last:
                errors.append(f"L{i}: empty Last Name")
            if not title:
                errors.append(f"L{i}: empty Title")
            if not company:
                errors.append(f"L{i}: empty Company Name")
            if not email:
                errors.append(f"L{i}: empty Email")
            elif not EMAIL_RE.match(email):
                errors.append(f"L{i}: malformed Email: {email}")
            else:
                el = email.lower()
                if el in seen_emails:
                    errors.append(f"L{i}: duplicate Email: {email}")
                seen_emails.add(el)

            key = (first.lower(), last.lower())
            if first and last:
                if key in seen_names:
                    errors.append(f"L{i}: duplicate name: {first} {last}")
                seen_names.add(key)

    return errors


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv_path", type=Path, help="Path to outreach CSV")
    args = p.parse_args()
    if not args.csv_path.is_file():
        print(f"ERROR: file not found: {args.csv_path}", file=sys.stderr)
        return 2
    errors = validate(args.csv_path)
    if errors:
        print(f"FAIL ({len(errors)} issue(s))")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
