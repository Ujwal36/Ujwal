array = [10,30,20,29,65]

def revarray(array):
    i=0
    j=len(array)-1
    while i<j:

        temp = array[i]
        array[i]=array[j]
        array[j]=temp
        i = i+1
        j=j-1
    return array


    

print(revarray(array))