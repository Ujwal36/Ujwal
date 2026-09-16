#Reverse a dictionary
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

i = 0
j = 0
length = len(data.keys())
while j < length:
  k,v = tuple(data.items())[i]
  temp = k
  k,v = v,k
  data[k] = v
  del data[temp]
  j += 1
print(data)


