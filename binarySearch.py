

def binarysearch(n,key):
    low = 0
    high = len(n)-1
    while low <= high:

        mid = int((low + high)/2)
        if key == n[mid]:
            return mid
        elif key < n[mid]:
            high = mid-1
        else:
            low = mid+1
n = [2,5,7,8,31,67]
key= 5
print(binarysearch(n,key))