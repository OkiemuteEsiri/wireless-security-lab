from __future__ import annotations

import argparse
import json
from pathlib import Path

from .engine import assess_devices
from .models import AccessPoint
from .reporting import render_markdown


def load_inventory(path: Path) -> list[AccessPoint]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("inventory root must be a list")
    return [AccessPoint(**item) for item in raw]


def main() -> int:
    parser = argparse.ArgumentParser(description="Assess authorized wireless inventory against a defensive security baseline.")
    parser.add_argument("inventory", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    findings = assess_devices(load_inventory(args.inventory))
    report = render_markdown(findings)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
