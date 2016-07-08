#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# luck.py - Opens several Google search results.

import requests
import sys
import webbrowser
import bs4

__author__ = "Teumer"

# Display text while downloading the Google page
print("Googling...")

res = requests.get("http://google.com/search?q={}".format(" ".join(sys.argv[1:])))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open("http://google.com{}".format(linkElems[i].get('href')))