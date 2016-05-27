#! python3
# downloads.py - example of using requests to download a file

import requests

link = "https://automatetheboringstuff.com/files/rj.txt"

# Request the file
res = requests.get(link)

# Check the download status
res.raise_for_status()

play_file = open("RomeoAndJuliet.txt", "wb")

for chunk in res.iter_content(100000):
    play_file.write(chunk)

play_file.close()
