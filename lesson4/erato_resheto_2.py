import cProfile

def resheto(n):
    #верхняя граница до скольки вычисляем простые числа
    till = 10000

    def prime(x):
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
    
    lst_prime = []

    for number in range(1,till):
        if prime(number):
            lst_prime.append(number)
            if lst_prime.index(number) == n:
                break

    return(lst_prime[n])

cProfile.run('resheto(50)')

#print(resheto(5))

#"erato_resheto_2.resheto(5)"
# 1000 loops, best of 3: 14.8 usec per loop

#"erato_resheto_2.resheto(50)"
# 1000 loops, best of 3: 673 usec per loop
