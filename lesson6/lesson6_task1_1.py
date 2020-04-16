#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.
from memory_profiler import profile
import sys
from mem_sum import sum_memory

def show_sizeof(x):
  return (sys.getsizeof(x))

@profile
def reverse(num):
  num_reversed = ''


  i = len(num)-1
  while i >= 0:
    num_reversed += ''.join(num[i])
    i -= 1

  mem = show_sizeof(num_reversed) + show_sizeof(i)
  print(f'Использовано памяти {mem} байт')
  print()
  print(sum_memory(locals(), verbose=True))
  return(f'Число после оборота {num_reversed}')


if __name__ == '__main__':
  reverse('5667808990003455677888999000567899009976655445679098765544333222')


# Использовано памяти 141 байт
# Filename: lesson2_task1_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#      9     14.5 MiB     14.5 MiB   @profile
#     10                             def reverse(num):
#     11     14.5 MiB      0.0 MiB     num_reversed = ''
#     12
#     13
#     14     14.5 MiB      0.0 MiB     i = len(num)-1
#     15     14.5 MiB      0.0 MiB     while i >= 0:
#     16     14.5 MiB      0.0 MiB       num_reversed += ''.join(num[i])
#     17     14.5 MiB      0.0 MiB       i -= 1
#     18
#     19     14.5 MiB      0.0 MiB     mem = show_sizeof(num_reversed) + show_sizeof(i)
#     20     14.5 MiB      0.0 MiB     print(f'Использовано памяти {mem} байт')
#     21     14.5 MiB      0.0 MiB     return(f'Число после оборота {num_reversed}')
