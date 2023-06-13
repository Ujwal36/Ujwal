def addDigits(num):
        num = str(num)
        num = [x for x in num]
        number =0
        while len(num) > 1:
            for x in num:
                number += int(x)
            num = [x for x in str(number)]
            number = 0
        num = "".join(num)
        return int(num)
n = 999
print(addDigits(n))