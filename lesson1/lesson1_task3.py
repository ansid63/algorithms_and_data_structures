#Написать программу, которая генерирует в указанных пользователем границах:
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.


import random

start_numbers,finish_numbers = input('Введи через пробел начало и конец ряда целых значений: ').split(' ')
start_numbers = int(start_numbers)
finish_numbers = int(finish_numbers)
print(random.randrange(start_numbers, finish_numbers, 1))

start_float,finish_float = input('Введи через пробел начало и конец ряда вещественных значений: ').split(' ')
start_float = float(start_float)
finish_float = float(finish_float)
print(random.uniform(start_float, finish_float))

start_letter,finish_letter = input('Введи через пробел начало и конец ряда латинских букв: ').split(' ')
start_letter = ord(start_letter)
finish_letter = ord(finish_letter)
find_letter = chr(random.randrange(start_letter, finish_letter))
print(find_letter)