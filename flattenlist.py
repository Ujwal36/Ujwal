#Flatten the list with depth 
nums = [1, [2, 3], [4, [5, 6]], [[7, 8], 9]]

def flatten(nums):
  output = []
  for num in nums:
    if isinstance(num,list):
      flatten(num)
    else:
      output.append(num)
  return output

print(flatten(nums))
