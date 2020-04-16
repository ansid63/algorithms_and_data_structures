# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.

import random
import operator

size = 10
array = [(random.randint(0, 50)) for i in range(size)]

print(array)


def merge_sort(lst):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = len(lst) // 2
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])
        #print(left, right)
        return merge(left, right)




def merge(left, right, compare=operator.lt):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

print(merge_sort(array))