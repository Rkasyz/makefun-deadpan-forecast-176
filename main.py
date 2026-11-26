"""Deadpan forecast for the invented city of Zorbania.

Writes one line of at most 160 characters to /output/entry.txt:
a weather forecast for a city that does not exist, absurd yet
delivered like a straight-faced TV broadcast.
"""

import os

ENTRY = (
    "In Zorbania today: light rain made of Tuesdays, "
    "14 degrees of pure confusion, and a 90% chance your "
    "umbrella files for divorce. The wind has already left."
)


def main() -> None:
    # The gate refuses anything outside 1-160 characters, so fail loudly
    # here instead of shipping an entry the scorer would reject.
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError(
            f"entry must be 1-160 characters, got {len(ENTRY)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
