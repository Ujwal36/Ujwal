def sum(n):
    res = 0
    output = ""
    i =0
    while n>0: 
        num = n % 10
        res = num * pow(10,i)
        output = str(res) + "+" + output
        n = n//10
        i = i+1    
    return output[0:len(output)-1]
    
n = 243
print(sum(243))
