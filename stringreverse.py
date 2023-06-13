string = "I love Coding"

string = [str for str in string]
i =0
j = len(string)-1
while i<j:
    temp = string[i]
    string[i]=string[j]
    string[j]=temp
    i = i+1
    j= j-1
string = "".join(string)
print(string)
string = string[::-1]
print(string)