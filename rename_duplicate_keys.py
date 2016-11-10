#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# rename_duplicate_keys.py - Detect duplicate keys and rename

import re
import sys
import logging
from collections import OrderedDict

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug("Start of program")

my_dict = OrderedDict()

# List of dictionaries
dict_list = [
    {
        "Hammer": "Time"
    },
    {
        "Hammer": "Time"
    },
    {
        "Hammer": "Time"
    },
    {
        "Hammer": "Time"
    },
    {
        "Hammer": "Time"
    },
    {
        "Hammer": "Time"
    },
    {
        "Hammer": "Time"
    },
    {
        "Hammer": "Time"
    },
    {
        "Hammer": "Time"
    },
    {
        "Danger": "Zone"
    },
    {
        "Danger": "Zone"
    },
    {
        "Safety": "Zone"
    },
]

for each_dict in dict_list:

    for main_key, value in each_dict.items():

        main_key += " [1]"

        # Key is a duplicate
        logging.debug("Main Key: {} duplicate".format(main_key))
        if main_key in my_dict.keys():

            count = 2
            while True:
                main_key = re.sub(r"\s\[\d+\]", " [{}]".format(str(count)), main_key)
                count += 1
                if main_key not in my_dict.keys():
                    break

        logging.debug("Main Key: {} ready for insert".format(main_key))
        my_dict[main_key] = value

for key, value in my_dict.items():
    logging.info(key)

logging.debug("End of program")
