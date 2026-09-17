# Given a string, count the occurrence of each character and replace duplicates:  
#   - Input: "Automation" 
#   - Output: "2u22m22i2n"

input = "Automation"

dict = {}

for ch in input:
  ch = ch.lower()
  if ch in dict.keys():
    dict[ch] = dict[ch] + 1
  else:
    dict[ch] = 1
output = ""
print(dict)
for ch in input:
  ch = ch.lower()
  if dict[ch] > 1:
    output += str(dict[ch])

  else:
    output += ch
print(output)
