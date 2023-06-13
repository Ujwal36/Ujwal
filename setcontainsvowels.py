from re import S


def containsvowels(list):
    setvowels = {'a','e','i','o','u'}
    count =0
    dict={}
    print(list)
    for s in list:
        for ch in s:
            if ch in setvowels:
                count +=1
        dict.update({s: count})
        count =0
    print(dict)


s = "I love coding and debugging"
containsvowels(s.split(" "))
