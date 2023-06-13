def sumofeven(n):
    if n == 2 or n==3:
        return 2
    if n % 2 == 0:
        return n + sumofeven(n-2)
    else:
        return (n-1) + sumofeven(n-3)
n = 7
print(sumofeven(n))