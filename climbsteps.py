def climbsteps(n) -> int:


        if n ==1 or n ==2:
            return n
        else:
            return climbsteps(n-1) + climbsteps(n-2)

n = 5
print(climbsteps(n))



