#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.
from memory_profiler import profile
import sys
from mem_sum import sum_memory

def show_sizeof(x):
  return (sys.getsizeof(x))

@profile
def reverse(num):


    num_reversed = ''

    lst = []

    for i in num:
          lst.append(i)

    lst.reverse()

    for j in lst:
        num_reversed += ''.join(j)

    mem = show_sizeof(num_reversed) + show_sizeof(lst)
    print(f'Использовано памяти {mem} байт')
    print()
    print(sum_memory(locals(), verbose=True))
    return (f'Число после оборота {num_reversed}')

if __name__ == '__main__':
    reverse('5667808990003455677888999000567899009976655445679098765544333222')



# Использовано памяти 753 байт
# Filename: lesson2_task1_2.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#      8     14.5 MiB     14.5 MiB   @profile
#      9                             def reverse(num):
#     10
#     11
#     12     14.5 MiB      0.0 MiB       num_reversed = ''
#     13
#     14     14.5 MiB      0.0 MiB       lst = []
#     15
#     16     14.5 MiB      0.0 MiB       for i in num:
#     17     14.5 MiB      0.0 MiB             lst.append(i)
#     18
#     19     14.5 MiB      0.0 MiB       lst.reverse()
#     20
#     21     14.5 MiB      0.0 MiB       for j in lst:
#     22     14.5 MiB      0.0 MiB           num_reversed += ''.join(j)
#     23
#     24     14.5 MiB      0.0 MiB       mem = show_sizeof(num_reversed) + show_sizeof(lst)
#     25     14.5 MiB      0.0 MiB       print(f'Использовано памяти {mem} байт')
#     26     14.5 MiB      0.0 MiB       return (f'Число после оборота {num_reversed}')
