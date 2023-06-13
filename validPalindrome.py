# Valid Palindrome: Remove all the characters other than alpha numeric characters and the resulting string should read the same back and forth.
import re
def validpal(s):

        pattern = "[0-9a-zA-Z]"
        s = re.findall(pattern,s)
        s = "".join(s)
        i =0 
        j = len(s)-1
        print(s)
        while(i<j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

str = "0p"
print(validpal(str))