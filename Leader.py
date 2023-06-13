# A Leader in an array is defined as an element which is greater than all the elements to its left. Find such leaders.

def leader(a):
    leader = []
    for x in a:
        if a.index(x) == 0:
            leader.append(x)
        elif x > max(leader):
            leader.append(x)
    print(leader)
a = [-1,9,3,4,6,9]
leader(a)
        