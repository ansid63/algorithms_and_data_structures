# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

lst = list(range(2,99+1))
num = list(range(2,9+1))

for item in num:
    sum = 0
    for var in lst:
        if var % item == 0:
            sum += 1
    print(f'В массиве {sum} чисел кратно {item}')