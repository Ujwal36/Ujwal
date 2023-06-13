# a given integer of any leangth. Right shift the given integer, the given number of times,n.
# Eg: Right shift 125789 n=3 times --> 912578 891257 789125
import string
def rightshiftinteger(integer,n):
    list = ""
    list = str(integer)
    list = [x for x in list]
    k = len(list)-1
    while n > 0:
        
        result = [0]*(k+1)
        for i in range(0,len(list)):
            result[(i+1)%(k+1)] = list[i]
        print(result)
        list = result
        n -= 1
       


integer = 125789
n = 3
rightshiftinteger(integer,n)