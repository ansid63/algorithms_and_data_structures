# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

lst = [random.randint(0, 100) for item in range(20)]

print(f'Массив случайных чисел {lst}')

max = 0

i = 0
j = 2

# Находим максимальное значение
while i < len(lst):
    if lst[i] > lst[i-1] and lst[i] > max:
        max = lst[i]
    i += 1

# Ввел стартовое минимальное значение
if lst[1] > lst[0]:
    min = lst[0]
elif lst[0] > lst[1]:
    min = lst[1]

# Находим минимальное значение
while j < len(lst):
    if lst[j] < lst[j-1] and lst[j] < min:
        min = lst[j]
    j += 1  

print(f'Максимальное число {max}')
print(f'Минимальное число {min}')

# Костыль для корректного вывода
new_lst = list(lst)
new_lst[lst.index(max)] = min 
new_lst[lst.index(min)] = max

print(f'Массив после изменений {new_lst}')
