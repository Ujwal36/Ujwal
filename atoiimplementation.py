import re
def myatoi(s):
        s = s.strip()
        result = ""
        pattern = "^[+-]?[0-9]+"
        list = re.findall(pattern,s)
        print(list)
        if(len(list) == 0):
            return 0
        s = "".join(list)
        print(s)
        s = int(s)
        return s

s= "-987 is a negative."
print(myatoi(s))
