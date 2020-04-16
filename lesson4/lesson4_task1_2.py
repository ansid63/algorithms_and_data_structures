# Определить, какое число в массиве встречается чаще всего.
import random
import cProfile

def max_num(n):
    lst = [random.randint(1, 11) for i in range(n)]
    #print(lst)

    # Находим максимальное значение
    mini = min(lst)
    # Находим минимальное значение
    maxi = max(lst)


    #лист для подсчета количества вхождений
    count_list = [0 for i in range(mini, maxi+1)]
    #print(count_list)

    for item in lst:
        count_list[item-mini] += 1

    bol = (max(count_list))
    return (mini + count_list.index((bol)))

#cProfile.run('max_num(50)')
#print(max_num(50))

#"lesson4_task4_2.max_num(50)"
# 1000 loops, best of 3: 80.3 usec per loop

#"lesson4_task4_2.max_num(100)"
# 1000 loops, best of 3: 153 usec per loop