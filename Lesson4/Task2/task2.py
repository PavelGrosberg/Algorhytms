# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»


"""
Простой алгоритм имеет квадратичную сложность, а решето - логарифмическую, поэтому при малом значении n -
разница в скорости выполнения практически отсутствует и вырастает в десятки раз с увеличением n.
"""


from time import time


def simple_number(n):               # O(n2)
    counter = 0
    num = 1
    while counter < n:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            counter += 1
    return num


def sieves(N, n):                    # O(n log(log n))
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False
    simple = []
    for k in range(N):
        if A[k]:
            simple.append(k)
    return simple[n-1]



print(simple_number(10))
print(sieves(30, 10))

def time_func(func, *arg, repeats=10**4):
    result = []
    for _ in range(repeats):
        start = time()
        func(*arg)
        stop = time()
        time_taken = stop - start
        result.append(time_taken)
    return sum(result) / len(result)


number = 10
numbers = 30
my_alg_time = time_func(simple_number, number,  repeats=1000)
sieve_time = time_func(sieves, numbers, number, repeats=1000)
print(f'Результат вычисления {number}-го простого числа\n'
      f'Время простого алгоритма: {my_alg_time:.2e}\n'
      f'Время решета: {sieve_time:.2e}\n'
      f'Соотношение: {my_alg_time / sieve_time:.2f}\n')

number = 100
numbers = 1000
my_alg_time = time_func(simple_number, number,  repeats=1000)
sieve_time = time_func(sieves, numbers, number, repeats=1000)
print(f'Результат вычисления {number}-го простого числа\n'
      f'Время простого алгоритма: {my_alg_time:.2e}\n'
      f'Время решета: {sieve_time:.2e}\n'
      f'Соотношение: {my_alg_time / sieve_time:.2f}\n')

number = 1000
numbers = 10000
my_alg_time = time_func(simple_number, number,  repeats=1000)
sieve_time = time_func(sieves, numbers, number, repeats=1000)
print(f'Результат вычисления {number}-го простого числа\n'
      f'Время простого алгоритма: {my_alg_time:.2e}\n'
      f'Время решета: {sieve_time:.2e}\n'
      f'Соотношение: {my_alg_time / sieve_time:.2f}\n')
