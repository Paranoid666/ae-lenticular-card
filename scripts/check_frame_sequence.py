"""Check nonempty, contiguous AE frame filenames without image dependencies."""

import argparse
import json
import re
from pathlib import Path


def check(directory, prefix, extension, start, count):
    if not directory.is_dir():
        raise ValueError(f"Frame directory does not exist: {directory}")
    if start < 0 or count <= 0:
        raise ValueError("start must be nonnegative and count must be positive")
    pattern = re.compile(re.escape(prefix) + r"(\d+)\." + re.escape(extension.lstrip(".")), re.I)
    found = {}
    empty = []
    for path in directory.iterdir():
        match = pattern.fullmatch(path.name)
        if path.is_file() and match:
            number = int(match[1])
            found.setdefault(number, []).append(path.name)
            if path.stat().st_size == 0:
                empty.append(path.name)
    expected = set(range(start, start + count))
    missing = sorted(expected - found.keys())
    unexpected = sorted(found.keys() - expected)
    duplicates = {str(k): v for k, v in sorted(found.items()) if len(v) > 1}
    return {
        "ok": not (missing or unexpected or duplicates or empty),
        "expected_count": count,
        "found_numbers": len(found),
        "missing": missing,
        "unexpected": unexpected,
        "duplicates": duplicates,
        "empty_files": sorted(empty),
        "scope": "Filename continuity and nonzero size only; pixels and video are not decoded.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--extension", default="tif")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--count", type=int, required=True)
    args = parser.parse_args()
    try:
        result = check(args.directory, args.prefix, args.extension, args.start, args.count)
    except (ValueError, OSError) as error:
        parser.exit(2, f"{error}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
