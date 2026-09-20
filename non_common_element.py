# Find which element is not present in list2 but in list1
list1 = [1,2,3,4]
list2 = [1,2,3,5]
dup = True
for i in range(len(list1)):
  if list1[i] ^ list2[i]:
    dup = False
    ele = list1[i]
    break
print(dup, ele)
