# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).


import random


def bubble_sort(li):
    for n in range(1, len(li) - 1):
        for i in range(len(li) - n):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]


random.seed(42)

some_list = [random.randint(-100, 99) for _ in range(1000)]
print(some_list)
bubble_sort(some_list)
print(some_list)
