#Remove spaces in between in a given string

import re
s = "a a aa"
pattern = "\s+"
s= re.split(pattern,s)
s = "".join(s)
print(s)