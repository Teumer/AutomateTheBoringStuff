import re


check_phone_number = re.compile(r'\d{3}-\d{3}-\d{4}')

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
find = check_phone_number.findall(message)
for num in find:
    print("Phone number found: {}".format(num))
