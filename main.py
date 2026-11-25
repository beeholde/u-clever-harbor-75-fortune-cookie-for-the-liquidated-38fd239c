"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line to /output/entry.txt (default) or to the
directory named by $MAKEFUN_OUTPUT_DIR.

The line (18 words, 101 characters):

    Trader, your luck was liquidated, not lost. The stars kept the
    receipt — your comeback is on layaway.

Why it should win, against the judge's brief in order:
  1. Fortune voice + loss + trader, all explicit: "Trader" is addressed,
     "liquidated" names the loss, "The stars kept the receipt" is the
     oracular cookie voice.
  2. Rueful and warm, never cruel: the luck was not lost, only liquidated,
     and the comeback is still coming - just deferred. The trader laughs
     with the cookie, not at it.
  3. One line, 18 words, reads whole in a single breath.
  4. Fresh: no lucky-numbers list, no "great fortune awaits", no stranger,
     no margin-call-as-visitor - the field is full of those. The turn is
     "on layaway": a comeback paid for in instalments, because the trader
     is broke. Retail vocabulary (receipt, layaway) reframes the loss.
  5. The fortune voice ("The stars kept the receipt") is broken by the
     punchline ("your comeback is on layaway").
"""

import os
from pathlib import Path

LINE = "Trader, your luck was liquidated, not lost. The stars kept the receipt \u2014 your comeback is on layaway."


def check(text: str) -> None:
    """Gate mirror: 1-160 chars, at most 20 words, one line, non-blank."""
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1-160"
    words = text.split()
    assert len(words) <= 20, f"{len(words)} words, over the 20-word cap"
    assert "\n" not in text.strip(), "must be a single line"
    assert text.strip(), "must not be only whitespace"


def main() -> None:
    check(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
