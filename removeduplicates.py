def removeduplicates(a):
    
    list = []
    
        
    for val in a:
        if val not in list:
            list.append(val)
    
    return list
    

a = [1,3,5,7,1]
str = "automation"
print(removeduplicates(a))
