# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

natural_numbers = range(2, 100)
divider = range(2, 10)
result = []

for k in divider:
    count = 0

    for n in natural_numbers:
        if n % k == 0:
            count += 1
    result.append((k, count))

# print('В указанном промежутке:')
# for num, count in result:
#     print(f'{num} кратно {count} числам')

