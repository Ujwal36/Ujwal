def merge(a,b):
    i=0
    j=0
    res = []
    while i < len(a) and j<len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            if a[i]==b[j]:
                j=j+1
            i = i+1
        
    if i == len(a):
        for x in range(j,len(b)):
            res.append(b[x])
    else:
        for x in range(i,len(a)):
            res.append(a[x])
    return res

a = [1,2,3,4,5,6,7,8]
b=  [1,2,3,4,5,6,7,8]
print(merge(a,b))