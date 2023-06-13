import re
def timeConversion(s):
    # Write your code here
    pattern = "\d+:\d+:\d+"
    clockrange = re.search(pattern,s)
    clockvalue = s[clockrange.start():clockrange.end()]
    clock = clockvalue.split(":")
    clock24 = ""
    print(s)
    if s.endswith("AM"):
        if clock[0] == '12':
            clock24 = "00:" +clock[1]+ ":"+ clock[2]
        else:
            clock24 = clock[0]+ ":" +clock[1]+ ":"+ clock[2]
    else:
        if clock[0] == '12':
            hour = 12
        else:
            hour = int(clock[0]) + 12
        clock24 = str(hour) + ":" + clock[1]+ ":"+ clock[2]
    return clock24
s = "12:09:07PM"
print(timeConversion(s))