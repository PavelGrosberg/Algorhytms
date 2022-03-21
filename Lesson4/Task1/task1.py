# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Задача №4 из второго урока.


from time import time
import sys


def count_cycle_for(n):    # O(n)
    result = 0
    number = 1
    for _ in range(n):
        result += number
        number = number / (-2)
    return result


def count_cycle_while(n):    # O(n)
    result = 0
    number = 1
    while n > 0:
        result += number
        number = number / (-2)
        n -= 1
    return result


def count_recursion(m, n=1):
    if m == 1:
        return n
    else:
        return n + count_recursion(m - 1, n / (-2))


def time_func(func, arg, repeats=100):
    result = []
    for _ in range(repeats):
        start = time()
        func(arg)
        stop = time()
        time_taken = stop - start
        result.append(time_taken)
    return sum(result) / len(result)


sys.setrecursionlimit(1903)
reps = 1900
time_cycle_for = time_func(count_cycle_for, reps)
print(time_cycle_for)
time_cycle_while = time_func(count_cycle_while, reps)
print(time_cycle_while)
time_recursion = time_func(count_recursion, reps)
print(time_recursion)
print(f'Цикл for in быстрее цикла while в {time_cycle_while / time_cycle_for:.2f} раз(а)')
print(f'Цикл while быстрее рекурсии в {time_recursion / time_cycle_while:.2f} раз(а)')
print(f'Цикл for быстрее рекурсии в {time_recursion / time_cycle_for :.2f} раз(а)')
