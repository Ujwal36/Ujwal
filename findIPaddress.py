#str = "This is the IP 192.168.5.5"
f = open("ipaddress.txt","rt")

pattern = "(((25[0-5|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\\.){3})(25[0-5|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
#pattern = "((((\d{1,3})\\.){3})(\d{1,3}))"
import re
for x in f:

    val = re.search(pattern,x)
    print(val.start(),val.end())
result =""
for i in range(val.start(),val.end()):
    result += x[i]
print(result)
f.close()
# File for writing:

f = open("ipaddress.txt","wt")
f.writelines(result)

f.close()