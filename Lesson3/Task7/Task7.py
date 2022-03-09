# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

from random import randint

some_list = [randint(0, 99) for i in range(10)]
result = sorted(some_list)[:2:]

print(some_list)
print('Два наименьших числа из списка:', result)
