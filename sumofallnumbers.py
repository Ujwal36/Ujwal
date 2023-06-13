def sumofall(number):
    string = str(number)
    sum = 0
    liststr = [x for x in string]
    while len(liststr) > 1:

        for x in liststr:
            sum = sum + int(x)
        liststr.clear()
        liststr = [x for x in str(sum)]
        sum = 0
        print(liststr)
    print(liststr[0])

number = 0
sumofall(9999)