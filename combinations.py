def combination(s,k):
    string = ""
    for x in s:
        string  += x.strip()
    print(string)
    n = len(string)
    total = 0
    num = n
    for i in range(1,k):
        num = num * (n-1)
        n = n-1
    num = num/k
    return num
    
  




n = 4
s = "a a b c"
k = int(input())
print(combination(s,k))