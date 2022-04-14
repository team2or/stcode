
from collections import deque
a = 0
b = 3
edges = [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]]
edges = sorted(edges, key=lambda x:x[1])
print(edges)

n = 8
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for i in edges:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
print(graph)
q = deque()
q.append((0,a))

def bfs():
    while q:
        c, num = q.popleft()
        visited[num] = True
        for i in graph[num]:
            if not visited[i]:
                q.append((c+1, i))
            if i == b:
                return c+1

answer = []
def dfs(a, b, graph, visited):
    q = deque()
    q.append([0,a])
    visited[a] = True
    answer.append(a)
    while q:
        c, now = q.popleft()
        print(now)
        for i in graph[now]:
            if not visited[i]:
                q.append([c+1, i])
                visited[i] = True
            if i == b:
                return c+1
dfs(a, b, graph, visited)