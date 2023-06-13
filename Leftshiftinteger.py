# Left shift given integer , given number of times, n
# integer = 125678 n=3, --> 256781, 567812, 678125

def leftshift(integer,n):
    list = str(integer)
    list = [x for x in list]
    k = len(list)-1
    result = [0] * len(list)
    while n>0:
        for i in range(0,len(list)):
                result[i] = list[(i+1)%(k+1)]
        n -= 1
        print(result)
        list = result
        result = [0] * len(list)
integer = 125678
leftshift(integer,3)