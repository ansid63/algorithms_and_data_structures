#Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите натуральное число: ')

result_chet = 0
result_nechet = 0

i = 0
while i < len(num):
    if int(num[i]) == 0 or int(num[i])%2 ==0:
        result_chet += 1
    else:
        result_nechet += 1
    i += 1 


print(f'Количество четных чисел {result_chet}, количество нечетных чисел {result_nechet}')