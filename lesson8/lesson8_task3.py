# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.



n = int(input('Введи количество вершин у графа '))


# Функция создает граф в виде списка смежности
def graf_gener(v):
    graf = {}
    points = [i for i in range(v)]
    for i in range(v):
        temp = points.copy()
        temp.remove(i)
        graf[i] = temp
    
    return graf


graf = graf_gener(n)
print(graf)

# Конвертация списка смежности в обычный граф
grafin = [[0 for i in range(n)] for j in range(n)]

for k, v in graf.items():
    for i in v:
        grafin[k][i] = 1

print(*grafin, sep='\n')


# Функция обходит не взвешенный ориентированный граф по алгоритму поиска в глубину
visited = [False] * n

def dfs(start):
    visited[start] = True
    for v in grafin[start]:
        if not visited[v]:
            dfs(v)

ncomp = 0
for i in range(n):
    if not visited[i]:
        ncomp += 1
        dfs(i)




