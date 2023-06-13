def twosum(a,target):
    map = {}
    i=0
    for val in a:
        compliment = target - val
        if compliment in map.keys():
            return i,map.get(compliment) 
        else:
            map.update({val:i})
            i = i+1

a=[1,2,3,9,7]
target = 8
print(twosum(a,target))