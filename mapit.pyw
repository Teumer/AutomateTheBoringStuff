#! python3
# mapit.pyw - Launches a map in the browser using an address from the command line or clipboard.

import sys
import pyperclip
import webbrowser

# Get address from command line
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])

# Get the address from the clipboard
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/{}".format(address))
