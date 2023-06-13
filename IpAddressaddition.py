ip = "10.124.250.250"
octets = ip.split(".")
octets = [int(x) for x in octets]
octetindex = 3

while octetindex >= 0:
    if int(octets[octetindex]) < 255:
        octets[octetindex] += 1
    else:
        octetindex -= 1

print(octets)