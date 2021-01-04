def my_func(num_1: float, num_2: float) -> float:

    if num_2 == 0:
        print('Деление на 0 невозможно.\n')
        return 0
    else:
        return round(((num_1 / num_2)),2)


num_1 = input('Введите делимое число:')
num_2 = input('Введите делитель:')
print(my_func(int(num_1), int(num_2)))
