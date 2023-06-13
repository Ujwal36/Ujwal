def removeduplicatesstring(string):
    list = []
    output = ""
    for s in string:
        if s not in list:
            list.append(s)
    return output.join(list)

string = "automation"
print(removeduplicatesstring(string))