#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. 
#Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

# Использовал два модуля collections. Получилось много кода, предпологаю что есть решение попроще :)

from collections import namedtuple
from collections import defaultdict

average_companinies = defaultdict(int)

n = int(input('Сколько компаний участвует в оценке '))
i = 0

# В цикле создаем компании с параметрами через namedtuple, считаем сумму дохода по компании и всё это вставляем в defaultdict
while i < n:
    param = input('Введи название и выручку за 4 квартала через пробел, пример: Danone 546 523 452 123 ').split()
    New_company = namedtuple('New_company', 'name qv1 qv2 qv3 qv4')
    company1 = New_company._make(param)
    #print(company1)
    sum_company = int(company1.qv1) + int(company1.qv2) + int(company1.qv3) + int(company1.qv4)
    #print(sum_company)
    average_companinies[company1.name] = sum_company
    i+=1

print(average_companinies)

sum = 0
for k, v in average_companinies.items():
    sum += v

average_full = sum/n

print(f'Среднее значение прибыли по всем предприятиям {average_full}')

low_profit = []
high_profit = []

for k, v in average_companinies.items():
    if  v < average_full:
        low_profit.append(k)
    elif v >= average_full:
        high_profit.append(k)

print(f'Компании с прибылью выше среднего {high_profit}, компании с прибылью ниже среднего {low_profit}')


