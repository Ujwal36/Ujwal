import re
string = "04:00:00pm"
pattern = "[^PMAMpmam]"
search = re.findall(pattern,string)

print("".join(search))
