import random # импортирую библиотеку

n = int(input("Enter N: ")) # получаю значение от пользователя
numbers = [random.randint(1, 100) for _ in range(n)] # заполняю список случайными значениями

print(f"Original list: {numbers}") # изначальный список
print(f"Sum: {sum(numbers)}") # сумма всех элементов
print(f"Average: {sum(numbers) / len(numbers):.2f}") # среднее значение всех элементов списка
print(f"Minimum: {min(numbers)}") # минимум
print(f"Maximum: {max(numbers)}") # максимум

numbers.sort() # сортирую список
print(f"Sorted: {numbers}")

unique = list(dict.fromkeys(numbers))
print(f"Without duplicates: {unique}")
