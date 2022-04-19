#해커랭크
#복습
#Symmetric Pairs
#https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true
#답안참고
#https://pearlluck.tistory.com/503
SELECT F1.X, F1.Y FROM Functions F1 JOIN Functions F2 ON F1.X=F2.Y AND F1.Y=F2.X
GROUP BY F1.X, F1.Y
HAVING count(F1.X) > 1 OR F1.X < F1.Y
ORDER BY F1.X;

#프로그래머스
#BFS
#게임 맵 최단거리
#https://programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
def solution(maps):
    r = len(maps)
    l = len(maps[0])
    dist = [[0]*l for i in range(r)]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    q = deque([(0,0)])
    while q:
        x, y = q.popleft()
        maps[x][y] = 0
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx and nx < r and 0 <= ny and ny < l:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
    if dist[-1][-1] == 0:
        return -1
    else:
        return dist[-1][-1] +1

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])