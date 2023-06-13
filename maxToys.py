# Given amount k and given a list of toys with cost. Find the max toys that can be bought for given k

def maxtoys(k,list):
    current = []
    currentsum =0
    for item in list:
        if item < k:
            if currentsum <= k:
                current.append(item)
                currentsum += item
            else:
                maxinlist = max(current)
                currentsum -= maxinlist
                current.remove(maxinlist)
                current.append(item)
                currentsum += item
    return current
list = [38, 29,50,100,1,2,3,46,5,99]
k = 40
print(maxtoys(k,list))