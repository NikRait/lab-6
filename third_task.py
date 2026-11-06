matrix = [
    [1, 2, 3, 4, 7],
    [4, 5, 6, 6, 7],
    [7, 8, 9, 7, 7]
] # Матрица

# Через zip
transposed = [list(row) for row in zip(*matrix)] #  Меняем столбцы и строки местами с помощью функции zip()

# Output
print("Origin matrix: ")
for row in matrix:
    print(row)

print("\nTransposed matrix: ")
for row in transposed:
    print(row)
