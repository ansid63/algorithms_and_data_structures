# Определить, какое число в массиве встречается чаще всего.
import random

lst = [random.randint(1, 10) for i in range(50)]

print(lst)

nums = {}

# в словарь подставляем в пару ключ: значение, число: количество повторов
for item in lst:
    if item not in nums.keys():
        nums[item] = 1
    elif item in nums.keys():
        nums[item] += 1
  
print(nums)

# выводим число с максимальным количеством повторов
max_key = max(nums, key=nums.get)
  
print(f'Чаще всего встречается число {max_key}')