# To merge 2 lists of integers and the resulting array has no duplicates

def merge(a,b):
    c = []
    i = 0
    j =0
    a.sort()
    b.sort()
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            if a[i] not in c:
                print("i ",i, "a[i]" ,a[i])
                c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if b[j] not in c:
                print("j ",j, "b[j]" ,b[j])
                c.append(b[j])
            j += 1
        else:
            if a[i] not in c:
                print("i ",i, "a[i]" ,a[i])
                c.append(a[i])
            i += 1
            j += 1

    if i < len(a):
        while i < len(a):
            if a[i] not in c:
                c.append(a[i])
            i += 1
    if j < len(b):
        while j < len(b):
            if b[j] not in c:
                c.append(b[j])
            j += 1
    print(c)
a = [1,2,5,6,5,9]
b = [9,1,2,7,6,5]
merge(a,b)
    