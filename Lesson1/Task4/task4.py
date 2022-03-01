import random

print('Ведите границы для случайного целого числа:')
x1 = int(input('x1 = '))
x2 = int(input('x2 = '))
print('Ведите границы для случайного вещественного числа:')
y1 = float(input('y1 = '))
y2 = float(input('y2 = '))
print('Ведите границы для случайной буквы:')
ch1 = input('char1 = ').upper()
ch2 = input('char2 = ').upper()

r_int = random.randint(x1, x2)
r_float = random.uniform(y1, y2)
r_char = chr(random.randint(ord(ch1), ord(ch2)))

print(f'Случайное целое число: {r_int}\n'
      f'Случайное вещественное число: {r_float}\n'
      f'Случайная буква: "{r_char}"')
