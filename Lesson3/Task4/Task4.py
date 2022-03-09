# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

some_list = [randint(0, 9) for i in range(10)]
numbers_dict = {}
for number in some_list:
    if number in numbers_dict:
        numbers_dict[number] += 1
    else:
        numbers_dict[number] = 1

max_enc_number = max(numbers_dict.items(), key=lambda x: x[1])

print(f'В списке {some_list}\nЧисло {max_enc_number[0]} встречается чаще всего: {max_enc_number[1]} раз(а)')
