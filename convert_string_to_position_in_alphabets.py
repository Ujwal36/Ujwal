# Return the positions of letters of a given input string as the output
name = "Ujwal"
res = []
alphabets = ""
for i in range(26):
  alphabets += chr(ord('a') + i)
print(alphabets)

dict = {}

for k,v in enumerate(alphabets,start=1):
  dict[v] = k
print(dict)
for char in name:
  char = char.lower()
  res.append(str(dict[char]))

print("-".join(res))




