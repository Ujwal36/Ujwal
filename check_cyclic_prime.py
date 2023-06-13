# A number is a cyclic prime if 197 , 719 and 971 are all prime numbers.
# Given a number n, find the count of cyclic primes <=n

def cyclicprime(n:int):
    count = 0
    for i in range(2,n+1):
        print("current number:", i)
        if isPrime(i) and isCyclic(i):
            count += 1
            print(i)
    return count
def isPrime(number:int):
    i = 2
    while i <= number//2:
        if number%i == 0:
            return False
        i +=1 
    return True
import string
def isCyclic(num):
    print("checking cyclic for:", num)
    s = str(num)
    if len(s) == 1:
        return True
    print("cyclic:", s)
    s = [x for x in s]
    k = len(s)
    count = 0
    while count < k-1:
        temp = s[0]
        for i in range(0,len(s)-1):
            s[i] = s[(i+1)]
        s[len(s)-1] = temp
        count += 1
        n = "".join(s)
        n = int(n)
        if not isPrime(n):
            return False
    return True

n= 100
print(cyclicprime(n))