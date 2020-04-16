# Определить, какое число в массиве встречается чаще всего.
import random
import cProfile

def max_num(n):
    lst = [random.randint(1, 10) for i in range(n)]

    #print(lst)

    nums = {}

    # в словарь подставляем в пару ключ: значение, число: количество повторов
    for item in lst:
        if item not in nums.keys():
            nums[item] = 1
        elif item in nums.keys():
            nums[item] += 1
    
    #print(nums)

    # выводим число с максимальным количеством повторов
    max_key = max(nums, key=nums.get)
    
    return(f'Чаще всего встречается число {max_key}')

#cProfile.run('max_num(50)')
#print(max_num(50))

#"lesson4_task4_1.max_num(50)"
# 1000 loops, best of 3: 105 usec per 

#"lesson4_task4_1.max_num(100)"
# 1000 loops, best of 3: 172 usec per loop