def threeSum(nums):
        output = set()
        result = []
        expression = 0
        i =0
        nums.sort()
        while i < (len(nums)-2):
            
            j = i+1
            k = len(nums) -1
            while j < k:
               
                    
                expression = nums[j] + nums[k] + nums[i]
                if expression > 0:
                    k -= 1
                elif expression < 0:
                    j += 1
                
                else:
                    output.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1    
                    
                    
                        
                
                
            i += 1 
        
       
        
        print(output)
nums = [-4,-4,-4,2,2,2,2]
threeSum(nums)