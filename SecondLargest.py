import sys
def secondLargestelement(array):
    length = len(array)
    firstlargest = -sys.maxsize-1
    secondlargest = -sys.maxsize-1
    if length <= 1:
        print("no presence of second largest element.")
        return
    else:
        
        

        for i in range (0,len(array)):
            if array[i] > firstlargest:
                secondlargest = firstlargest
                firstlargest = array[i]
            elif array[i] > secondlargest and array[i] != firstlargest:
                secondlargest = array[i]
    print(firstlargest, " ", secondlargest)

array = [3,4,4,3,4,2,4,3]
secondLargestelement(array)