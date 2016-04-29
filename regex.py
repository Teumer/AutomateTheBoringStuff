import re

# The ? matches zero or one of the preceding group.
# The * matches zero or more of the preceding group.
# The + matches one or more of the preceding group.
# The {n} matches exactly n of the preceding group.
# The {n,} matches n or more of the preceding group.
# The {,m} matches 0 to m of the preceding group.
# The {n,m} matches at least n and at most m of the preceding group.
# {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# \d, \w, and \s match a digit, word, or space character, respectively.
# \D, \W, and \S match anything except a digit, word, or space character, respectively.
# [abc] matches any character between the brackets (such as a, b, or c).
# [^abc] matches any character that isn’t between the brackets.

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

# optional
batman_search = re.compile(r'Bat(wo)?man')
message = "The Adventures of Batman"
find = batman_search.search(message).group()
print(find)
message = "The Adventures of Batwoman"
find = batman_search.search(message).group()
print(find)
