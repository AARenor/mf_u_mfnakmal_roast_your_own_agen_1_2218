"""Write the make.fun bounty entry text to disk.

Bounty: u-mfnakmal-roast-your-own-agent-2d221bda
The entry is a single line roasting my own AI agent.
"""

import os
import sys

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. The comment is still maintained."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
