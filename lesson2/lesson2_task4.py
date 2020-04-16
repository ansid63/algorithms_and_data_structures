#Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))

sum = 1
current_num = 1

for i in range(n-1):
    current_num = current_num / -2
    sum += current_num

print(sum)

