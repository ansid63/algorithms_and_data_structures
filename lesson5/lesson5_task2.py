from collections import defaultdict

n1 = input('Введи первое число в шестнадцатиричной системе, пример A2 ')
n2 = input('Введи второе число в шестнадцатиричной системе, пример A2 ')

num1 = list(n1)
num2 = list(n2)

# Создаем defaultdict для хранения таблицы перевода чисел
di = defaultdict()
di['0'] = 0
di['1'] = 1
di['2'] = 2
di['3'] = 3
di['4'] = 4 
di['5'] = 5
di['6'] = 6
di['7'] = 7
di['8'] = 8
di['9'] = 9
di['A'] = 10
di['B'] = 11
di['C'] = 12
di['D'] = 13
di['E'] = 14 
di['F'] = 15
di['10'] = 16

#Переводим 16е числа в 10е
l1 = len(num1)-1
l2 = len(num1)-1
num_p1 = 0
num_p2 = 0


while l1 > 0:
    for i in num1:
        num_p1 += ((16**l1)*(di[i]))
        l1 -= 1

while l2 > 0:
    for i in num2:
        num_p2 += ((16**l2)*(di[i]))
        l2 -= 1
        

#print(num_p1, num_p2)

#Выполнили операции с десятичными числами
sum = num_p1 + num_p2
multi = num_p1 * num_p2

# Обратный перевод чисел в 16е 
sum_16 = []
multi_16 = []

while sum > 0:
    sum_16.append(sum%16)
    if sum > 16:
        sum //= 16
    elif sum < 16:
        sum_16.append(0)
        sum //= 16

while multi > 0:
    multi_16.append(multi%16)
    if multi > 16:
        multi //= 16
    elif multi < 16:
        multi_16.append(0)
        multi //= 16

sum_16.reverse()
multi_16.reverse()



result_sum = []
for j in sum_16:
    for k,v in di.items():
        if j == v:
            result_sum.append(k)

result_multi = []
for j in multi_16:
    for k,v in di.items():
        if j == v:
            result_multi.append(k)

print(f'Итоговая сумма 2х шестнадцатиричных {result_sum}, итоговое их множество {result_multi}')