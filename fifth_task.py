list_1 = [1, 2, 3, 4, 6, 7]
list_2 = [1, 2, 8 ,9, 0, 6]

set_1 = set(list_1)
set_2 = set(list_2)

union = set_1 | set_2
intersection = set_1 & set_2
difference = set_1 - set_2

print(f"Union = {sorted(union)}")
print(f"Intersection = {sorted(intersection)}")
print(f"Difference = {sorted(difference)}")
