import sys


def sum_memory(objects, verbose=True):
    sum_mem = 0
    for item in objects:
        if item.startswith('__'):
            continue
        elif hasattr(objects[item], '__call__'):
            continue
        elif hasattr(objects[item], '__loader__'):
            continue
        else:
            sum_mem += sys.getsizeof(objects[item])
            if verbose:
                print(f'Переменная{item}, \tкласс = {type(objects[item])}, \tзначение = {objects[item]};'
                      f'\tзанимает {sys.getsizeof(objects[item])} байт ')

    return f'Переменные заняли {sum_mem} байт'
