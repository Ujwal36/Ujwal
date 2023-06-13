s=['I','love','coding']
int=[3,5,6]
output =""
for j in int:

    
    for str  in s:
        
        for ch in str:
            for i in range(0,j):
                output = output + ch
    
print(output)
