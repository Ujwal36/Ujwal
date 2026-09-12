#Write a python program to output the following result for :
# input: names = ["Ana ", " boB", "ANA", "bob", " Cal"]
# output: {'ana': 2, 'bob': 2, 'cal': 1} - With out using dictionary built-in functions

names = ["Ana ", " boB", "ANA", "bob", " Cal"]
dict = {}
for name in names:
  name = name.strip().lower()
  if name not in dict:
    dict[name] = 1
  else:
    dict[name] = dict[name] + 1
print(dict)

name = "aabbbcaacc"
dict = {}
for ch in name:
  if ch not in dict:
    dict[ch] = 1
  else:
    dict[ch] = dict[ch]  +1
print(dict)
list = [k+str(v) for k,v in dict.items()]
print("".join(list))
