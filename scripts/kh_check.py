#!/usr/bin/env python3
"""Check whether Cambodian legislation PDFs yield usable Khmer Unicode text.

Usage: kh_check.py FILE.pdf [...]
Prints, per file, the number of Khmer-block characters, COENG signs (U+17D2, needed for
subscript consonants), U+FFFD replacement characters and Latin-extended "legacy font" glyphs
in the extracted text (pdftotext). Text is only usable when Khmer characters dominate, COENG
signs are present and replacement / legacy glyphs are absent.
"""
import re
import subprocess
import sys

for f in sys.argv[1:]:
    t = subprocess.run(["pdftotext", "-l", "5", f, "-"], capture_output=True).stdout.decode("utf-8", "replace")
    kh = len(re.findall(r"[ក-៿]", t))
    coeng = t.count("្")
    repl = t.count("�")
    legacy = len(re.findall(r"[\u0080-˿]", t))
    ok = kh > 200 and coeng > kh / 40 and repl == 0 and legacy < kh / 50
    print(f"{f}\tkhmer={kh}\tcoeng={coeng}\treplacement={repl}\tlegacy={legacy}\t{'USABLE' if ok else 'NOT USABLE'}")
