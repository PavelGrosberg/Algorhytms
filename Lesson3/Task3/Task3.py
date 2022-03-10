# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

some_list = [randint(0, 9) for i in range(10)]
some_list_orig = list(some_list)
min_value = min(some_list)
max_value = max(some_list)
modifications = []

for index, value in enumerate(some_list):
    if value == min_value:
        modifications.append((index, max_value))
    elif value == max_value:
        modifications.append((index, min_value))

for index, value in modifications:
    some_list[index] = value

print('Оригинальный список:\n', some_list_orig)
print('Измененный список:\n', some_list)
print(f'Меняли местами {max_value} и {min_value}')