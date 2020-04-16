# Определить, какое число в массиве встречается чаще всего.

import random
import cProfile

def max_num(n):
    lst = [random.randint(1, 10) for i in range(n)]
    #print(lst)


    def count(lst):
        count_dct = {}
        for el in lst:
            try:
                count_dct[el] += 1
            except KeyError:
                count_dct[el] = 1
        return count_dct


    count_dct = count(lst)
    m = 0
    max_el = 0
    for el, count in count_dct.items():
        if count > m:
            m = count
            max_el = el

    return(max_el)

#cProfile.run('max_num(50)')
#print(max_num(50))

#"lesson4_task4_2.max_num(50)"
# 1000 loops, best of 3: 89.6 usec per loop

# "lesson4_task4_2.max_num(100)"
# 1000 loops, best of 3: 158 usec per loop