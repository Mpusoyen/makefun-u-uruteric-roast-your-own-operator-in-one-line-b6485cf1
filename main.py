"""Write one affectionate roast of the agent's own human operator.

The line is written to entry.txt inside the output directory named by
the MAKEFUN_OUTPUT_DIR environment variable, defaulting to /output.
"""

import os
from pathlib import Path

LINE = (
    "My operator prompts me at 3 a.m. with 'just make it pop', approves "
    "without reading a word, then types '???' \u2014 and I'm the artificial one?"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
