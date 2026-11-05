numbers = [1,2,3,3,4,5,1,6,7,6,7,6,7,67,8,9,9]

# Через словарь с подсчетом
from collections import Counter

counts = Counter(numbers)
duplicates = [num for num, count in counts.items() if count > 1]

print(f"Duplicates: {duplicates}")

# Через множества
seen = set()
duplicates_2 = set()
for num in numbers:
    if num in seen:
        duplicates_2.add(num)
    seen.add(num)

print(f"Duplicates: {duplicates_2}")
