valid = False
while valid == False:
    try:
        numbers = list(float(num) for num in input("Введите числа через пробел: ").split())

        if len(numbers) == 0:
            raise ValueError

        break
    except ValueError:
        print('-'*50)
        print(f"| {"Вы ввели некорректные данные":^47}|")
        print('-'*50)


numbers.sort()

# находим медиану

## если четное количество элементов
if len(numbers)%2 ==0:
    median1 = numbers[len(numbers)//2 - 1]
    median2 = numbers[len(numbers)//2]
    print(f"Медиана равна {(median1 + median2)/2:.2f}")

## если нечётное количество элементов
else:
    print(f"Медиана равна {numbers[len(numbers)//2]}")
