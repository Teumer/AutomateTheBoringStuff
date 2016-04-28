import re


check_phone_number = re.compile(r'(\d{3})-(\d{3}-\d{4})')
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
find = check_phone_number.findall(message)
for num in find:
    print("Phone number found: {}".format(num))

check_names = re.compile(r'joe|john')
message = "my name is joe, not john"
find = check_names.search(message)
print(find.group(0))

red_search = re.compile(r'red(robin|hat|october)')
message = "went to redrobin for lunch, redoctober standing by in october"
find = red_search.findall(message)
for hit in find:
    print(hit)
