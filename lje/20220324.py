#해커랭크
#Weather Observation Station 18
#https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true
SELECT round(abs((min(LAT_N) - max(LAT_N)) + (min(LONG_W) - max(LONG_W))),4) FROM STATION;

#Placements
#https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
#Packages테이블을 각각 Students와 Friends테이블에 JOIN하여 비교
#Packages테이블과 Friends테이블을 JOIN할땐 Friends테이블의 Friend_ID와 JOIN해야함
#친구의 Salary로 ORDER BY해야함
SELECT S.Name FROM Students S LEFT JOIN Friends F ON S.ID = F.ID
LEFT JOIN Packages P1 ON S.ID = P1.ID
LEFT JOIN Packages P2 ON F.Friend_ID = P2.ID
WHERE P1.Salary < P2.Salary
ORDER BY P2.Salary;

#[참고]
#https://ehdals9412.tistory.com/35

#백준
#DFS/BFS
#케빈 베이컨의 6단계 법칙
#https://www.acmicpc.net/problem/1389
#[참고]
#https://fre2-dom.tistory.com/156

from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                #실제 단계보다 +1해서 추가됨
                visited[i] = visited[x] + 1
                q.append(i)

result = []
for i in range(1,n+1):
    visited = [0] * (n+1)
    bfs(i)
    result.append(sum(visited))
print(result.index(min(result))+1)


#다른 답안
#https://chaewsscode.tistory.com/98
import sys
from collections import deque


def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            #방문을 인덱스말고 해당 숫자가 있는지로 체크해서 확인
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    result = []
    for i in range(1, n+1):
        result.append(bfs(graph, i))

    print(result.index(min(result))+1)