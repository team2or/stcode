#해커랭크
#복습
#New Companies
#https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
SELECT C.company_code, C.founder, count(DISTINCT LM.lead_manager_code), count(DISTINCT SM.senior_manager_code), count(DISTINCT M.manager_code), count(DISTINCT E.employee_code) FROM Company C
JOIN Lead_Manager LM ON C.company_code = LM.company_code
JOIN Senior_Manager SM ON C.company_code = SM.company_code
JOIN Manager M ON C.company_code = M.company_code
JOIN Employee E ON C.company_code = E.company_code
GROUP BY C.company_code, C.founder
ORDER BY C.company_code;

#백준
#유기농배추
#https://www.acmicpc.net/problem/1012
from collections import deque
T = int(input())
def bfs(array, a, b):
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    q = deque([(a,b)])
    array[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx and nx < n and 0 <= ny and ny < m:
                if array[nx][ny] == 1:
                    array[nx][ny] = 0
                    q.append((nx,ny))
for t in range(T):
    m,n,k = map(int, input().split())
    array = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        array[y][x] = 1
    answer = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                answer += 1
                bfs(array, i, j)
    print(answer)

