n = 7
m = 3
count = 0
res = 0
while m:
    if m % 2 ==1:
        res += n << count 
        print(n)
        
    count  = count + 1
    m = int(m//2)
    print('m is', m)
print(res)