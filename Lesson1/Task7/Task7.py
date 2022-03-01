


print('Введите длины трех отрезков:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не существует')
elif a != b and a != c and b != c:
    print('Треугольник разносторонний')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print("Равнобедренный")
