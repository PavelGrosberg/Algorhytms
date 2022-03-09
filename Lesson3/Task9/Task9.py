# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

ROWS = 3
COLUMNS = 3

random_matrix = [[randint(0, 99) for _ in range(COLUMNS)] for __ in range(ROWS)]

print('Матрица: ')
for row in random_matrix:
    for num in row:
        print(f'{num: >2d}', end=' ')
    print('')

min_in_col_list = []
for i in range(len(random_matrix[0])):
    min_in_col_list.append(min(random_matrix, key=lambda x: x[i])[i])
print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', max(min_in_col_list))