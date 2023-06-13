def pattern(n):
    res = ""
    j=0
    while j < n:

        for i in range (0,n):
            if i % 2 ==0:
                res = res + "W"
            else:
                res = res + "B"
        res = res + "\n"
        j = j + 1
    return res.strip()
n=10
print(pattern(n))