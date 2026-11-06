list_1 = [1, 2, 3, 4, 6, 7]
list_2 = [1, 2, 8 ,9, 0, 6]
# Initialization of 2 lists
set_1 = set(list_1) # Set of first list
set_2 = set(list_2) # Set of second list

union = set_1 | set_2 # Finding union of those sets
intersection = set_1 & set_2 # Finding intersection of those sets
difference = set_1 - set_2 # Finding intersection of those sets

print(f"Union = {sorted(union)}")
print(f"Intersection = {sorted(intersection)}")
print(f"Difference = {sorted(difference)}")
# Printing values that we got
