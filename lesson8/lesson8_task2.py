# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
from collections import defaultdict



g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

# В этом defaultdict буду хранить путь к точке
#way = defaultdict(list)


def dijkstra(graf, start):
    lengh = len(graf)
    is_visited = [False] * lengh
    cost = [float('inf')] * lengh
    parant = [-1] * lengh

    cost[start] = 0
    min_cost = 0
    

    while min_cost < float('inf'):
        is_visited[start] = True
        
        for i, vertex in enumerate(graf[start]):
            if vertex != 0 and not is_visited[i]:
                
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parant[i] = start
                    #way[i].append(parant[i])


        min_cost = float('inf')
        for i in range(lengh):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
        
    result = [[] for _ in range(lengh)]

    for i in range(lengh):
        if is_visited[i]:
            result[i].append(i)
            j = i
            while parant[j] != -1:
                result[i].append(parant[j])
                j = parant[j]

            result[i].reverse()       
      
        

    return cost, result



s = int(input('От какой вершины идти '))
cost, path = dijkstra(g,s)
print(cost)
for k,v in enumerate(path):
    print(f'до точки {k} можно пройти через {v}')


# Видоизменяю словарь чтобы был виден весь маршрут
# for k,v in way.items():
#     if v[0] in way.keys():
#         way[k].extend(way[v[0]])
#     v.sort()

# for k, v in way.items():
#     print(f'К точке {k} можно прийти через {v}')


