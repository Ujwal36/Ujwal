def encodestring(string):
    count =1
    output = ""
    for i in range(0,len(string)-1):
        if string[i]!= string[i+1]:
            output = output + str(count) + string[i]
            count = 1
        else:
            count = count + 1
    output = output + str(count) + string[len(string)-1]
    return output
string = "aabbccc"
print(encodestring(string))