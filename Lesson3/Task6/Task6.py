# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

some_list = [randint(0, 9) for i in range(10)]
max_idx = max(enumerate(some_list), key=lambda x: x[1])[0]
min_idx = min(enumerate(some_list), key=lambda x: x[1])[0]
step = 1 if min_idx < max_idx else -1
result = sum(some_list[min_idx + step:max_idx:step])

some_list[max_idx] = f'*{some_list[max_idx]}*'
some_list[min_idx] = f'*{some_list[min_idx]}*'

print(some_list)
print('Сумма:', result)
