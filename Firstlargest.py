def firstLargest(array):
    if len(array) > 0:
        max = array[0]
        for element in range(1,len(array)):
            if array[element] > max:
                max = array[element]
        print(max)
    else:
        print("array is empty and cannot find max element in that")
        
    

array = [1,99999999]
firstLargest(array)