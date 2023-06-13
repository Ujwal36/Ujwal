def maxof3(list):
    a,b,c = list
    return a if a > b and a > c else b if b > c else c
list = [1,3,9]
print(maxof3(list))