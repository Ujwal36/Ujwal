num = 12345
output = 0
while num > 0 :
  rem = num%10
  output = output * (10) + rem
  num //= 10
  print(output)
