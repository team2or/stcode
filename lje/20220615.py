#프로그래머스_SQL
#복습
#고양이와 개는 몇 마리 있을까
#https://programmers.co.kr/learn/courses/30/lessons/59040
#각 type별로 그룹지어 count 후 고양이를 먼저 조회해야하므로 order by로 알파벳 순으로 조회
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE;

#NULL 처리하기
#https://programmers.co.kr/learn/courses/30/lessons/59410
#IFNULL과 CASE WHEN 두가지 방법으로 품
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name"), SEX_UPON_INTAKE FROM ANIMAL_INS;
SELECT ANIMAL_TYPE, CASE WHEN NAME IS NULL THEN "No name" ELSE NAME END, SEX_UPON_INTAKE FROM ANIMAL_INS;


#백준
#깊이너비우선탐색
#현수막
#https://www.acmicpc.net/problem/14716
from collections import deque
m, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(m)]

def bfs(x, y):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    q = deque()
    q.append([x,y])
    array[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx and nx < m and 0 <= ny and ny < n:
                if array[nx][ny] == 1:
                    array[nx][ny] = 0
                    q.append([nx, ny])

cnt = 0
for i in range(m):
    for j in range(n):
        if array[i][j] == 1:
            cnt += 1
            bfs(i,j)
print(cnt)