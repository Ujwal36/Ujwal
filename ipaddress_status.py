import re
dict = {}
file = open("iplog.txt","rt")
ip = []
ippattern = "((((25[0-5|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3})(25[0-5|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]))"
status_pattern = "[a-zA-Z\s]+"
for record in file:
    ip = re.search(ippattern,record)
    ip = record[ip.start():ip.end()]
    status = re.search(status_pattern,record)
    status = record[status.start() : status.end()]
    print("ip", ip ,"status ", status)
    if ip not in dict.keys():
        dict.update({ip: status})
    elif status!= dict.get(ip):
        dict.update({ip: status})
print(dict)