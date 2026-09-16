# create a dictionary from a list
keys = ["name", "age", "city"]
values = ["Ujwal", 35, "Bangalore"]
output = {}
for k,v in zip(keys,values):
  output[k] = v

print(output)
