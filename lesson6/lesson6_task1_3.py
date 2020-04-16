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

    #print(lst)

    dct = {}
    j = len(lst)
    i = 0

    while j > 0:
        dct[i] = lst[j-1]
        j -= 1
        i += 1
    #print(dct)

    for v in dct.values():
        num_reversed += ''.join(v)

    mem = show_sizeof(num_reversed) + show_sizeof(lst) + show_sizeof(j) + show_sizeof(dct) + show_sizeof(i)
    print(f'Использовано памяти {mem} байт')
    print()
    print(sum_memory(locals(), verbose=True))
    return (f'Число после оборота {num_reversed}')

if __name__ == '__main__':
    reverse('5667808990003455677888999000567899009976655445679098765544333222')


# Использовано памяти 3085 байт
# Filename: lesson2_task1_3.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#      9     14.5 MiB     14.5 MiB   @profile
#     10                             def reverse(num):
#     11
#     12     14.5 MiB      0.0 MiB       num_reversed = ''
#     13
#     14     14.5 MiB      0.0 MiB       lst = []
#     15
#     16     14.5 MiB      0.0 MiB       for i in num:
#     17     14.5 MiB      0.0 MiB           lst.append(i)
#     18
#     19                                 #print(lst)
#     20
#     21     14.5 MiB      0.0 MiB       dct = {}
#     22     14.5 MiB      0.0 MiB       j = len(lst)
#     23     14.5 MiB      0.0 MiB       i = 0
#     24
#     25     14.5 MiB      0.0 MiB       while j > 0:
#     26     14.5 MiB      0.0 MiB           dct[i] = lst[j-1]
#     27     14.5 MiB      0.0 MiB           j -= 1
#     28     14.5 MiB      0.0 MiB           i += 1
#     29                                 #print(dct)
#     30
#     31     14.5 MiB      0.0 MiB       for v in dct.values():
#     32     14.5 MiB      0.0 MiB           num_reversed += ''.join(v)
#     33
#     34     14.5 MiB      0.0 MiB       mem = show_sizeof(num_reversed) + show_sizeof(lst) + show_sizeof(j) + show_sizeof(dct) + show_sizeof(i)
#     35     14.5 MiB      0.0 MiB       print(f'Использовано памяти {mem} байт')
#     36     14.5 MiB      0.0 MiB       return (f'Число после оборота {num_reversed}')
