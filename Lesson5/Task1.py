# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.



import collections

enterprise = collections.namedtuple('Enterprise', ['name', 'income_1', 'income_2', 'income_3', 'income_4'])

e_list = []
e_list.append(enterprise('Roga', 11.1, 22.2, 33.3, 44.4))
e_list.append(enterprise('And', 55.5, 66.6, 77.7, 88.8))
e_list.append(enterprise('Kopyta', 99.9, 100.00, 110.10, 120.20))


avg = sum([sum(i[1:5]) for i in e_list]) / len(e_list)
avg_above = [i[0] for i in e_list if sum(i[1:5]) >= avg]
avg_below = [i[0] for i in e_list if sum(i[1:5]) < avg]

print(f'Предприятия, чья годовая прибыль выше средней: {avg_above}')
print(f'Предприятия, чья годовая прибыль ниже средней: {avg_below}')

