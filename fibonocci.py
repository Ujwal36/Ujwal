n = 100
fibcache = [0] * (n+1)

def fib(n):
    if n<=1:
        return n
    if fibcache[n] !=0:
        return fibcache[n]
    nthfibonoccinumber = fib(n-1) + fib(n-2)
    fibcache[n] = nthfibonoccinumber
    return nthfibonoccinumber

print(fib(n))