class Solution:
    import sys
    def reverse(x) -> int:
        sum = 0
        s = abs(x)
        s = str(s)
        s=s[::-1]
        print(s)
        s = int(s)
        if  s > 2147483647:
            return 0
        return s if x > 0 else -s
    x = -123456
    print(reverse(x))

   
   

