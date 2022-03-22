#해커랭크
#Weather Observation Station 16
#https://www.hackerrank.com/challenges/weather-observation-station-16/problem?isFullScreen=true
SELECT round(min(LAT_N), 4) FROM STATION WHERE LAT_N > 38.7780;

#Weather Observation Station 17
#https://www.hackerrank.com/challenges/weather-observation-station-17/problem?isFullScreen=true
SELECT round(LONG_W, 4) FROM STATION WHERE LAT_N = (SELECT min(LAT_N) FROM STATION WHERE LAT_N > 38.7780);

#format으로 자리수 지정을 하려고 했지만 min()을 사용해서 그런지 반올림된다.
#format(LONG_W, '#.0000')가 아닌 format(LONG_W, 4)으로 하니 된다.

#백준
#DFS/BFS
#연결 요소의 개수
#https://www.acmicpc.net/problem/11724
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v, graph, visited):
    q = deque([v])
    visited[n] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

count = 0
for v in range(1, n+1):
    if not visited[v]:
        dfs(v, graph, visited)
        count += 1
print(count)
