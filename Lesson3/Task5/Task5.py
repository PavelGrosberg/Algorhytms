# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

some_list = [randint(-10, 10) for i in range(10)]

max_neg_number = max([i for i in some_list if i < 0])
print(f'В списке\n{sorted(some_list)}')
print(f'максимальное отрицательное число: {max_neg_number}')
