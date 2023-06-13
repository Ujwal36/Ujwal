
def efficientJanitor(weight):
    # Write your code here
    n = len(weight)
    current = weight[0]
    count = 0
    for i in range(1,n):
        if current + weight[i] > 3.00:
            count  = count + 1
            current = weight[i]
        else:
            current = current + weight[i]
            print(current)

        
    count = count + 1
    return count

        
    
weight= [1.00, 0.99 , 1.00 , 0.01]
print(efficientJanitor(weight))

