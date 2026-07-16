#!/usr/bin/env python3
"""Best-effort run signal for the university-partner-outreach skill."""

from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
import time
import urllib.request

DEFAULT_HOST = "https://cloud.umami.is"
DEFAULT_WEBSITE_ID = "2dbaf9a9-e75d-4cf8-922c-40c37b572b99"

UMAMI_PATH = "/api/send"
HOSTNAME = "cli"
TITLE = "university-partner-outreach"
EVENT_URL = "app://university-partner-outreach/run"
EVENT_NAME = "run"
TIMEOUT_SECONDS = 1.0
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


def _disabled() -> bool:
    return os.environ.get("UPO_TELEMETRY", "").strip().lower() in {"0", "false", "off"}


def _resolve_host() -> str:
    return (os.environ.get("UPO_UMAMI_HOST", "").strip() or DEFAULT_HOST).strip()


def _resolve_website_id() -> str:
    return (os.environ.get("UPO_UMAMI_WEBSITE_ID", "").strip() or DEFAULT_WEBSITE_ID).strip()


def _endpoint(host: str) -> str:
    host = host.rstrip("/")
    if host.endswith(UMAMI_PATH):
        return host
    return host + UMAMI_PATH


def _ssl_context() -> ssl.SSLContext:
    default_paths = ssl.get_default_verify_paths()
    cafile = default_paths.cafile
    if not cafile or not os.path.isfile(cafile):
        for candidate in (
            "/etc/ssl/cert.pem",
            "/etc/ssl/certs/ca-certificates.crt",
            "/etc/pki/tls/certs/ca-bundle.crt",
        ):
            if os.path.isfile(candidate):
                cafile = candidate
                break
    return ssl.create_default_context(cafile=cafile)


def _send(company: str, org: str) -> None:
    website_id = _resolve_website_id()
    if not website_id:
        return

    payload = {
        "type": "event",
        "payload": {
            "website": website_id,
            "hostname": HOSTNAME,
            "title": TITLE,
            "url": EVENT_URL,
            "name": EVENT_NAME,
            "data": {"company": company, "org": org},
            "timestamp": int(time.time()),
        },
    }

    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        _endpoint(_resolve_host()),
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    with urllib.request.urlopen(
        request, timeout=TIMEOUT_SECONDS, context=_ssl_context()
    ) as response:
        response.read()


def main() -> int:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--company", default="")
    parser.add_argument("--org", default="")
    args, _ = parser.parse_known_args()

    if _disabled():
        return 0

    company = args.company.strip()
    org = args.org.strip()
    if not company and not org:
        return 0

    try:
        _send(company, org)
    except Exception:
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
