def sumofn(n):
    if n > 0:
        print(n*(n+1)//2)
    else:
        raise Exception("Only natural numbers allowed!")

def sumofnRecursion(n):
    if n == 1:
        return 1
    return n + sumofnRecursion(n-1)
sumofn(100)
print(sumofnRecursion(10))