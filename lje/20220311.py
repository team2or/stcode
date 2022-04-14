#해커링크
#Population Density Difference
#https://www.hackerrank.com/challenges/population-density-difference/problem?isFullScreen=true
SELECT max(POPULATION)-min(POPULATION) FROM CITY;

#Revising Aggregations - The Sum Function
#https://www.hackerrank.com/challenges/revising-aggregations-sum/problem?isFullScreen=true
SELECT sum(POPULATION) FROM CITY WHERE DISTRICT = "California";

#백준
#DFS와 BFS
#https://www.acmicpc.net/problem/1260
#[참고]
#DFS, BFS: https://honggom.tistory.com/60
# https://happy-obok.tistory.com/m/14
from collections import deque

n,m,v = map(int,input().split())

line = {}
for _ in range(m):
    node = list(map(int, input().split()))
    if node[0] not in line:
        line[node[0]] = [node[1]]
    else:
        line[node[0]].append(node[1])
    if node[1] not in line:
        line[node[1]] = [node[0]]
    else:
        line[node[1]].append(node[0])

def bfs(line, v):
    visit = []
    queue = deque([v])
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            if node in line.keys():
                queue += sorted(list((set(line[node]) - set(visit))))
    return ' '.join(str(x) for x in visit)

def dfs(line, v):
    visit = []
    stack = [v]
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node in line.keys():
                stack += sorted(list((set(line[node]) - set(visit))),reverse=True)
    return ' '.join(str(x) for x in visit)

#프린트문으로 출력해야 함!!
#안그러면 틀렸다고 함
print(dfs(line,v))
print(bfs(line,v))

print(90//50)
print(90%50)