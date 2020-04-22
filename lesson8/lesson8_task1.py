# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

n = int(input('Введи число друзей участвовавших во встрече '))

# Создаём граф, все друзья встречаются в точке 0
grf = [[0 for j in range(n+1)] for i in range(n)]
for i in range(n):
    grf[i][0] = 1
print(*grf, sep='\n')

# Учел баг на встречу 1го друга
if len(grf) == 1:
    print('Мало друзей для рукопожатий')
else:
    # Проверяем кто из друзей был на встрече
    is_visited = [False for _ in range(len(grf))]

    for r in range(len(grf)):
        if grf[r][0] == 1:
            is_visited[r] = True


    # Считаем с кем встретился друг если был на встрече.
    count = 0

    for friend in range(len(grf)):
        if grf[friend][0] == 1:
            for visit in is_visited:
                if is_visited[visit]:
                    # Учитываем что не надо здороваться с собой :)
                    if visit == friend:
                        continue
                    count += 1
        




    print(f'Было {count/2} рукопожатий(ия/ие)')