def palint(integer):
    num = 0
    orig = integer
    while integer > 0:

        val = integer % 10
        num = (num * 10) + val
        integer = integer//10

    if num == orig:
        return True
    else:
        return False
integer = 121
print(palint(integer))
integer = 123
print(palint(integer))

import sys
i = sys.maxsize
print(i)
