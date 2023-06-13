from csv import list_dialects


a = [1,3,5,2,1,4,5,2]
listduplicaes = []
indices = []
for x in a :
    if x not in listduplicaes:
        listduplicaes.append(x)
    else:
        indices.append(a.index(x))
print(indices)
