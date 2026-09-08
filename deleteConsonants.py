# Program to delete all the consonants
vowels = {'A', 'E','I', 'O', 'U', 'a','e','i','o','u'}
name = "Python and Data Science"

name = [s for s in name]

i = 0
while i < len(name):
  if name[i] not in vowels and name[i] != ' ':
    name.remove(name[i])
   
  else:
    i+= 1
print("".join(name))
