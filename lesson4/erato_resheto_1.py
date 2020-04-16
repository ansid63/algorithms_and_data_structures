import cProfile

def resheto(n):
    #верхняя граница до скольки вычисляем простые числа
    till = 10000

    sieve = [i for i in range(till)]
    sieve[1] = 0

    for i in range(2, till):
        if sieve[i] != 0:
            j = i*2

            while j < till:
                sieve[j] = 0
                j += i

    pre_result = [i for i in sieve if i != 0]

    count = 0
    result = 0

    for item in pre_result:
        if item != 0:
            count += 1
            result = item
            if count == n:
                break

    return(result)

cProfile.run('resheto(5)')

#print(resheto(5))

#"erato_resheto_1.resheto(5)"
# 1000 loops, best of 3: 6.16 msec per loop

#"erato_resheto_1.resheto(50)"
# 1000 loops, best of 3: 6.36 msec per loop