#해커랭크
#Select By ID
#https://www.hackerrank.com/challenges/select-by-id/problem?isFullScreen=true
SELECT * FROM CITY WHERE ID = 1661;

#Japanese Cities' Names
#https://www.hackerrank.com/challenges/japanese-cities-name/problem?isFullScreen=true
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN';

#Average Population
#https://www.hackerrank.com/challenges/average-population/problem?isFullScreen=true
SELECT floor(avg(population)) FROM CITY;

#백준
#DFS/BFS
#토마토
#https://www.acmicpc.net/problem/7576
#[참고]
#https://jae04099.tistory.com/233
from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]

q = deque([])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx and nx < n and 0 <= ny and ny < m and box[nx][ny] == 0:
                #익히고 1을 더해주면서 다 익는데까지 얼마나 걸리는지 체크
                box[nx][ny] = box[x][y] + 1
                #익은 토마토가 있는 위치 추가
                q.append([nx,ny])

def result():
    count = 0
    bfs()
    for tomato in box:
        for num in tomato:
            if num == 0:
                return print(-1)
        count = max(count, max(tomato))
    return print(count - 1)

result()


