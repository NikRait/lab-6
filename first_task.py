import random

n = int(input("Enter N: "))
numbers = [random.randint(1, 100) for _ in range(n)]

print(f"Original list: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")

numbers.sort()
print(f"Sorted: {numbers}")

unique = list(dict.fromkeys(numbers))
print(f"Without duplicates: {unique}")
