from re import M
from turtle import st


def howMany(sentence):
    # Write your code here
    import re
    pattern = "\s+"
    alnumpattern = "[^a-zA-Z-,.?]"

    list = re.split(pattern,sentence)
    print(list)
    count =0
    for ele in list:
        if re.search(alnumpattern,ele):
            print(re.search(alnumpattern,ele))
            print(ele)
            count = count  + 1
    print(count)
    return len(list) - count
    
    
sentence = "jds       dsaf lkdf kdsa fkldsf, adsbf ldka ads? asd bfdal ds bf[l. akf dhj ds 878  dwa WE DE 7475 dsfh ds  RAMU 748 dj."
print(howMany(sentence))