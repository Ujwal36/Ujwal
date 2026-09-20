# Convert given text to replace vowels with its integer number in lexographical order
text = "automation is easy"
vowels = ['a','e','i','o','u']
dict = {}
alphabets = [chr(i) for i in range(ord('a'), ord('a')+26)]
print(alphabets)
for i,j in enumerate(alphabets, start=1):
  dict[j] = i
for ch in text:
  ch = ch.lower()
  if ch.isalpha() and ch in vowels:
    text = text.replace(ch, f"{str(dict[ch])}-")
print(text)
