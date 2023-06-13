import re
def extractnumbers(string):
    pattern = "\d"
    output = ""
    numbers = re.findall(pattern,string)
    for x in string:
        if x not in numbers:
            output = output + x            
    return output, numbers
string = "my 1st email id is ujwal36k@gmail.com and I created at the age of 20."

print(extractnumbers(string))