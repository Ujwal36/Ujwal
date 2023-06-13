from re import A


a = [5, 6, 0, 1, 0, 10, 0, 2, 0]
#Outpu= [5, 6, 1, 10, 2, 0, 0, 0, 0]

i=0
j=len(a)-1
def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    return a
while i<j:
    if a[i] == 0 and a[j] ==0:
        j = j-1
    elif a[i] !=0 and a[j] !=0:
        i = i+1
        j= j-1
    elif a[i] == 0 and a[j] !=0:
        a=swap(a,i,j)
    else:
        i= i +1



print(a)