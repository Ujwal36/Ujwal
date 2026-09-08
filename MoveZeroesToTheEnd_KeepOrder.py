# Python program to move all the 0's to the end of the list keeping other elements in the same order

nums = [0,0,12,3,0,9,0,1000,100,0,9]
count = nums.count(0)
print(count)
i =0 

while i<len(nums):
  if nums[i] == 0:
    nums.remove(nums[i])
  else:
    i += 1

list = [0] * count
nums.extend(list)
print(nums)
