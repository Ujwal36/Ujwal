# A leader in an array is an element which is greater than all the elements to its right
# Find such leaders

def leaderarray(a):
    list = []
    for i in range(len(a)-1,-1,-1):
        if len(list) == 0:
            list.append(a[i])
        elif a[i] > list[-1]:
            list.append(a[i])
    return list
a = [16, 17, 4, 3, 5, 2]
print(leaderarray(a))   