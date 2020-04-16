# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

lst = [random.randint(-20, 20) for i in range(20)]
print(f'Рандомный лист {lst}')

item = 0
min = -1

while item < len(lst):
    if lst[item] < 0 and min == -1:
        min = item
    elif lst[item] < 0 and lst[item] > lst[min]:
        min = item
    
    item += 1
        
  
print(f'Максимальный отрицательный элемент {lst[min]} стоит на позиции {min}')