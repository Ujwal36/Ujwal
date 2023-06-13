import string
def circularreverse(num:int):
    s =""
    number = 1971
    s = str(number)
    print(s)




    s = [x for x in s]
    k = len(s)
    count = 0
    while count < k-1:

        temp = s[0]
        for i in range(0,len(s)-1):
    
            s[i] = s[(i+1)]

        s[len(s)-1] = temp
        count += 1
        print(s)

num = 1971
circularreverse(num)


