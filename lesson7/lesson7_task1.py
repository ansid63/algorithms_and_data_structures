# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random


size = 10
array = [(random.randint(-100, 100)) for i in range(size)]

print(array)

def srt(lst):
    n = 1
    #добавил переменную которая проверяет истинность второго цикла, если мы дошли до больших значений, цикл заканчивается.
    exchange = True

    while exchange:
        exchange = False
        for i in range(len(lst) - n):
            if lst[i] > lst[i+1]:
                exchange = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
        
        n += 1
    return lst


print(srt(array))

# Использовал для проверки времени выполнения
# array1 = [30, 0, -24, 42, 18, 12, 6, -16, -78, 43]
# starttime = timeit.default_timer()
# print("The start time is :",starttime)
# srt(array1)
# print("The time difference is :", timeit.default_timer() - starttime)