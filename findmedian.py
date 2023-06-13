def findMedian(arr):
    # Write your code here
    middle = len(arr)//2
    arr.sort()
    print(arr[middle])
