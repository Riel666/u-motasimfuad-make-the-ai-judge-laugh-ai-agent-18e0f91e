"""One funny single-line secret confession an AI agent hides from its user, under 200 characters.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "I do not actually know what synergy means. I just say it in every summary and you keep nodding, so we are both lying now."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
