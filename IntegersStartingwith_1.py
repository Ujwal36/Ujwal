import re
import string
def startingWithOne(list):
    pattern = "^[1]"
    for x in list:
        s = str(x)
        if re.match(pattern,s):
            print(x)
list = [123,3001,11,1111,0 ,00]
startingWithOne(list)