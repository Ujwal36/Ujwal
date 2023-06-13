def binary(n):
    binary = ""
    while n>0:
        num = n % 2
        binary = str(num) + binary
        n = n//2
    return binary
n = 256
print(binary(n))