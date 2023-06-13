def countvowels(string):
    setvowels = {'a','e','i','o','u'}
    count = 0
    for ch in string:
        if ch in setvowels:
            count += 1
    dict ={}
    for ch in string:
        if ch in dict.keys():
           dict[ch] = dict.get(ch)+ 1
        else:
            dict.update({ch : 1})
    print(dict)
    return count
