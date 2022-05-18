#해커랭크
#복습
#The Report
#https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true
#BETWEEN으로 JOIN 후 CASE WHEN으로 Grade가 7이하일 때 "NULL"로 Name 출력
SELECT CASE WHEN G.Grade > 7 THEN S.Name ELSE "NULL" END, G.Grade, S.Marks FROM Students S JOIN Grades G WHERE S.Marks BETWEEN G.Min_Mark AND G.Max_Mark ORDER BY G.Grade DESC, S.Name;

#백준
#너비탐색
#섬의 개수
#https://www.acmicpc.net/problem/4963
#답안
#https://fullmoon1344.tistory.com/87
#기존에는 상하좌우만 했다면 이 문제는 대각선까지 포함
from collections import deque
# 시계 방향
def bfs(x, y):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    q = deque() #탐색을 하려는 좌표를 담는다.
    q.append([x, y])
    map_list[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx and nx < h and 0 <= ny and ny < w:
                if map_list[nx][ny] == 1:
                    map_list[nx][ny] = 0
                    q.append([nx,ny])

while True: 
    w, h = map(int, input().split())
    map_list = []
    cnt = 0
    if w == 0 and h == 0:
        break
    for _ in range(h):
        map_list.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if map_list[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)
