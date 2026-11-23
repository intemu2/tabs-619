#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes one number, digits only, to /output/entry.txt: the honest count of
open browser tabs. Deterministic: every run writes the exact same 3 bytes.
Standard library only; no network, no input, no arguments.
"""

import os

ENTRY = b"619"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(ENTRY)
    # Self-check: read back what was written and fail loudly if it differs,
    # so a partial or corrupted write never passes as a valid entry.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != ENTRY:
            raise SystemExit("entry.txt verification failed: written bytes differ")


if __name__ == "__main__":
    main()
