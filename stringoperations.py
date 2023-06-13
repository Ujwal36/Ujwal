def stringop(string):
    output = ""
    list = string.split(" ")
    print(list)
    for l in list:
        output = output + l[0].upper() + l[1:] + " "

   
    return output

string = "my name is ujwal"
print(stringop(string))

