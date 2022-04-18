#배달
import math
def solution(N, road, K):
    answer = 0
    visited = []
    distance = [0]+[math.inf for i in range(1,N)]
    roads = {i:{} for i in range(N)}

    for i in road:
        if i[1]  -1 in roads and i[0] -1 in roads[i[1]-1]:
            if roads[i[1]-1][i[0]-1] > i[2]:
                roads[i[1] - 1][i[0] - 1] = i[2]
                roads[i[0] - 1][i[1] - 1] = i[2]
        else:
            roads[i[1] - 1][i[0] - 1] = i[2]
            roads[i[0] - 1][i[1] - 1] = i[2]
    for j in roads[0]:
        distance[j] = roads[0][j]

    while len(visited) is not N:
        minimum = math.inf
        for i in range(1,N):
            if i not in visited and distance[i] < minimum:
                minimum = distance[i]
                town = i

        visited.append(town)
        for i in roads[town]:
            if distance[i] > distance[town] + roads[town][i]:
                distance[i] = distance[town] + roads[town][i]

    for k in distance:
        if k <= K:
            answer +=1
    return answer
solution(	6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4)