#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# search.py - Search files in current directory for text
#           - Example search.py "HARVEST_CODE" py

import re
import os
import sys

if len(sys.argv) != 3:
    raise Exception("Usage: search.py <search_keyword> <file_extension>")

keyword = sys.argv[1]
ext = sys.argv[2]

prog = re.compile(r"{}".format(keyword), re.IGNORECASE)
for file in os.listdir(os.getcwd()):
    if file.endswith(".{}".format(ext)):
        with open(file, "r") as f:
            if prog.search(f.read()):
                print("{}".format(file))
        f.close()
