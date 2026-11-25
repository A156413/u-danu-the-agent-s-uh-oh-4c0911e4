"""The Agent's Uh-Oh entry: one word an agent says when it has no idea what to do.

Deterministic: no network, no randomness, no clock. Writes the entry word
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it to stdout.
"""

import os
import stat

WORD = "recalculating"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(WORD)


if __name__ == "__main__":
    main()
