#해커랭크
#Japanese Cities' Attributes
#https://www.hackerrank.com/challenges/japanese-cities-attributes/problem?isFullScreen=true
SELECT * FROM CITY WHERE COUNTRYCODE = "JPN";

#Weather Observation Station 15
#https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true
SELECT round(LONG_W,4) FROM STATION WHERE LAT_N < 137.2345 ORDER BY LAT_N DESC LIMIT 1;

#다른답안
#https://velog.io/@develop_wan/MS-SQL-%ED%95%B4%EC%BB%A4%EB%9E%AD%ED%81%ACHacker-Rank-Weather-Observation-Station-15
#이중 SELECT문으로 137.2345보다 작은 LAT_N에서 가장 큰값을 max()로 선택
#round말고 format으로도 소수점 지정 가능
SELECT format(LONG_W, '#.0000') FROM STATION WHERE LAT_N = (SELECT max(LAT_N) FROM STATION WHERE LAT_N < 137.2345);

#백준
#DFS/BFS
#촌수계산
#https://www.acmicpc.net/problem/2644
#[참고]
#https://sorryhyeon.tistory.com/22
from collections import deque
n = int(input())
fp, sp = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
q.append((0,fp))

def bfs():
    while q:
        c, num = q.popleft()
        visited[num] = True
        for i in graph[num]:
            if not visited[i]:
                q.append((c+1, i))
            if i == sp:
                return c+1
    return -1

print(bfs())