# Sort the nums array evens at the beginning and odds at the end

nums = [1,3,5,7,9,11,0 , 0, 0 ,4,14,3,2,99,67,5,0,7,8, 80, 100]

i = 0
j = 0

while j < len(nums):
  if nums[j] % 2 ==0:
    i += 1
    j += 1
    
  else:
    while j < len(nums) and nums[j] %2 !=0:
      j += 1
    else:
      if j >= len(nums):
        break
      else:
        nums.insert(i,nums[j])
        j += 1
        del nums[j]
        i += 1
        j = i
        print(nums)
  print(i,j)
        
print(nums)
      
      
    
    
    
    
  
