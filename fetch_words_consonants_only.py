# Fetch words in a sentence which does not contain vowels
import re
text = "My name is ujwal and I am 35 years of age and my phone number is 97399939224"
output = []
pattern = ['a','e','i','o','u']

text = text.split(" ")
for word in text:
  cons = False
  for ch in word:
    if ch.lower() in pattern:
      cons = True
      break
  if not cons:
    output.append(word)
print(", ".join(output))
