# s  = (ab)2(a)3, output = ababaaa

def decoder(string):
    output = ""
    for i in string:
        if i == "(":
            stringtorepeat = ""
        elif i.isalpha():
            stringtorepeat += i
        elif i.isdigit():
            for j in range(0,int(i)):
                output = output + stringtorepeat
    return output
string = "(ab)2(a)3"
print(decoder(string))