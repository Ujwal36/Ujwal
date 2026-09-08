
# Write Python 3 code to encode last 5 digits of account number
# Here I have implemented using Caeser cipher method and improvisation
# 12 digit Account number
Account_number = "232801501100"
last_5_digit = Account_number[-5:]
print(last_5_digit)

def encode(last_5_digit):
  encoded_account_number = ""
  n = last_5_digit
  
  for ch in n:
    encoded_account_number += chr(ord('A') + int(ch))
  #Cipher
  key = "KEY"
  i = 0
  
  for char in encoded_account_number:
    k = key[i%3]
    i += 1

    print(chr(ord(char) + (ord(k) - ord('A'))))
    
  
  
  return Account_number[0:7] +encoded_account_number
print(encode(last_5_digit))
print(chr(49))
