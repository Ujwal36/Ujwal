# Find the factorial of a number

num = 100

def fact(num):
  if num < 2:
    return 1
  else:
    return fact(num-1) * num
print(fact(num))
