#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - loads all keywords to clipboard

import shelve
import pyperclip
import sys
import os

name = "mcb"
ext = [".dat", ".bak", ".dir", ".db"]
mcb_shelf = shelve.open(name)

num_of_args = len(sys.argv)
# Save clipboard content
if num_of_args == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
# Delete a saved key
elif num_of_args == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
elif num_of_args == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    # Clear everything
    elif sys.argv[1].lower() == 'clear':
        mcb_shelf.close()
        for ex in ext:
            try:
                os.remove(name + ex)
            except FileNotFoundError:
                pass
    # Recall saved content
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
