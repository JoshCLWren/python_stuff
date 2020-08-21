list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jeresey", "Rhode Island"]
combo = {list1[i]:list2[i] for i in range(0, len(list1))}
print(combo)