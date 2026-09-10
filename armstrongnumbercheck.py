#Check if a given number is armstrong

powered = lambda x,n: x**n

def is_armstrong(num):
  total = 0
  n = len(str(num)) #4
  number = str(num)
  for i in number:
    total += powered(int(i),n)
    print(total)
  return total == num

print(is_armstrong(num = 5))
