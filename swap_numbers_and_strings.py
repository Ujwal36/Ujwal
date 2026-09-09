#Swap 2 numbers

a = 10
b = 20

a = a + b
b = a-b
a = a - b

print(a,b)

# Swap 2 Strings

str1 = "bangalore"
str2 = "delhi"

str1 = str1 + str2 
str2 = str1[0:str1.find(str2)]
str1 = str1[str1.find(str2)+len(str2):]


print(str1,str2)





