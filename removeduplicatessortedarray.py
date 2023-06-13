def removeduplicatessortedarray(a):
    j=0
    print(len(a)-1)
    for i in range(0,len(a)-1):
        if a[i] != a[i+1]:
            a[j]=a[i]
            j = j+1
            i =i +1
        else:
            i = i + 1
        print(i,j,a)
    a[j] = a[len(a)-1]
    print(i,j,a)
    return a,j
a = [1,2,2,3,5,7,7,7]
a,j = removeduplicatessortedarray(a)
for i in range(0,j+1):
    print(a[i])