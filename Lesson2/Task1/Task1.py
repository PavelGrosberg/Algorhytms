# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный
# знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также
# сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


while True:
    operator = input("Введите знак операции (+, -, /, * или 0 для выхода): ")

    if operator == '0':
        break
    elif operator in {'+', '-', '/', '*'}:
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))
        if operator == '+':
            print(f'Сумма чисел равна {num_1 + num_2}')
        elif operator == '-':
            print(f'Разность чисел равна {num_1 - num_2}')
        elif operator == '/':
            if num_2 == 0:
                print('Ошибка, нельзя делить на ноль')
                continue
            else:
                print(f'Частное чисел равно {num_1 / num_2}')
        elif operator == '*':
            print(f'Произведение чисел равно {num_1 * num_2}')
    else:
        print('Ошибка, неверный знак!')
        continue