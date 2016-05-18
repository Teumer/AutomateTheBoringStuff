#!/bin/usr/python3
# number_clipboard.py - search for strings w/ 6 digits from the clipboard

import re
import pyperclip

text = str(pyperclip.paste())
prog = re.compile(r"\d{6}")
match = "\n".join(prog.findall(text))
print(match)
