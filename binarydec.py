list =[0, 0, 1, 1, 0, 1, 0]
decimal = 0
pos =-1
value = 0
for i in range(len(list)-1,0):
        print(list[i])
        if list[i] == 0:
            print("it is", 0)
            pos += 1
        else:
            pos += 1
            value = pow(2,pos)
            decimal += value
print(decimal)