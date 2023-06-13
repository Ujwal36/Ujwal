#S = “abcbba”


def pal(str):

    length = len(str)
    count =0
    if(length % 2 == 1):

        mid = length//2
        left = mid -1
        right = mid +1
        for i in range(0,mid):
            

            if str[left] != str[right]:
                count = count + 2
            left = left -1
            right = right + 1

    if(length % 2 == 0):
        mid = length//2-1
        left  = mid-1
        right = mid +2

        for i in range(0,mid-1):
            
            if str[mid] != str[mid+1]:
                count  = count  + 1
            if str[left] != str[right]:
                count = count + 1

            left = left -1
            right = right + 1

    
    print(count)

str = "aebcbda"

pal(str)