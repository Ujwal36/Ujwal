# Implement shallow copy vs deep copy

list1 = [1, 2, [3, 4]]
list2 = list1.copy()  # Shallow copy

list3 = list1[:]  # Another way to create a shallow copy

print("Original list:", list1)

list1[0] = 10  # Modify the first element of list1

list1[2][0] = 30  # Modify the nested list in list1

print("Shallow copy (list2):", list2)
print("Shallow copy (list3):", list3)

import copy
list4 = copy.deepcopy(list1)  # Deep copy
print("Deep copy (list4):", list4)
list1[2][1] = 40  # Modify the nested list in list1 again
print("After modifying list1 again:")   
print("Original list:", list1)
print("Deep copy (list4):", list4)

