# Sum of all the prime numbers in a given range
def sum_all_prime(low,high):
  sum = 0
  for i in range(low,high+1):
    if is_prime(i):
      sum += i
  return sum
def is_prime(num):
  for i in range(2,num//2+1):
    if num%i == 0:
      return False
  print(num)
  return True

print(sum_all_prime(3,100))
