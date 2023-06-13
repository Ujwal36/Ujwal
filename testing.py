set = set()
list = [1,2,3]
set.add((list[0],list[1],list[2]))
print(set)
set.add((list[1],list[2],list[0]))
print(set)