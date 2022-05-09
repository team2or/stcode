#프로그래머스
#복습
#오랜기간 보호한 동물(2)
#https://programmers.co.kr/learn/courses/30/lessons/59411
SELECT O.ANIMAL_ID, O.NAME FROM ANIMAL_OUTS O LEFT JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC LIMIT 2;

#2021카카오 인터십
#거리두기 확인하기
#https://programmers.co.kr/learn/courses/30/lessons/81302#fn1
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
from collections import deque
def bfs(place):
    start = []
    for i in range(len(place)):
        for j in range(len(place[0])):
            if place[i][j] == 'P':
                start.append([i,j])
    for s in start:
        q = deque([s])
        visited = [s]
        dist = [[0]*len(place[0]) for _ in range(len(place))]
        while q:
            dx, dy = [1,-1,0,0], [0,0,1,-1]
            x, y = q.popleft()
            for i in range(4):
                nx, ny = dx[i]+x, dy[i]+y
                if 0 <= nx and nx < len(place) and 0 <= ny and ny < len(place[0]) and [nx,ny] not in visited:
                    if place[nx][ny] == 'P' and dist[x][y] <= 1:
                        return 0
                    elif place[nx][ny] == 'O':
                        dist[nx][ny] = dist[x][y] + 1
                        visited.append([nx,ny])
                        q.append([nx,ny])
    return 1
answer = []
for place in places:
    answer.append(bfs(place))
print(answer)