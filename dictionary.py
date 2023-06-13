from itertools import count
def countstrings(string):
    dict = {}
    for x in string:
        if x in dict.keys():
            dict[x] = dict.get(x) + 1
        else:
            dict.update({x:1})
    print(dict)
    val= list(dict.values())
    key = list(dict.keys())
    val.sort(reverse=True)
    print(val)

    key.sort()
    print(key)
    output = []
    for v in val:
        for k in key:
            
            if dict.get(k) == v and k not in output:
                output.append(k)
        
    print(output)        
string = "394919399492992"
countstrings(string)