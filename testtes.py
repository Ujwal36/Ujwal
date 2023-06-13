
#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

def plusOne(digits):
        digit = 0
        i = len(digits)-1
        j =0
        while i >= 0:
            digit += digits[i] * (10 ** j)
            j += 1
            i -= 1
        digit += 1
        digit = str(digit)
        list = [int(x) for x in digit]
        return list
digits= [1,2,3,9]
print(plusOne(digits))