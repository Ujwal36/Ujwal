from re import I


def decimal(n):
    i =0
    decimal=0
    while n > 0:
        num = n % 10
        if num == 1:
            decimal = decimal + (num * pow(2,i))
        n = n//10
        i = i+ 1
    return decimal
n = 1111000
print(decimal(n))