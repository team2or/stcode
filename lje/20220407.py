#해커랭크
#복습
#Binary Tree Nodes
#https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
#이전답안
SELECT N, CASE WHEN P IS null THEN "Root"
WHEN N IN (SELECT DISTINCT P FROM BST) THEN "Inner"
ELSE "Leaf" END FROM BST ORDER BY N;

#concat으로 출력해도 됨
SELECT CASE WHEN P IS null THEN concat(N, " Root")
WHEN N IN (SELECT P FROM BST) THEN concat(N, " Inner")
ELSE concat(N, " Leaf") END FROM BST ORDER BY N;

#새문제
#SQL Project Planning
#https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true
#답안
#https://ysyblog.tistory.com/204
#https://techblog-history-younghunjo1.tistory.com/170
'''Start_Date 중 End_Date에는 없는 Start_Date는 각 연속적이지 않고 개별적으로 시작하는 프로젝트의 시작날짜를 의미한다.
End_Date 중 Start_Date에는 없는 End_Date는 각 연속적이지 않고 개별적으로 시작하는 프로젝트의 종료날짜를 의미한다.'''
SELECT Start_Date, MIN(End_Date) FROM
(SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) AS s, (SELECT End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) AS e
WHERE Start_Date < End_Date
GROUP BY Start_Date
ORDER BY DATEDIFF(MIN(End_Date), Start_Date), Start_Date;

#DATEDIFF
#https://extbrain.tistory.com/78
#날짜1 - 날짜2

#백준
#BFS
#영역 구하기
#https://www.acmicpc.net/problem/2583
#단지번호붙이기와 비슷
#직사각형의 좌표가 array좌표와 x,y값이 반대로 되어 있음

from collections import deque
n,m,k = map(int, input().split())
array = [[0]*m for _ in range(n)]
points = [list(map(int, input().split())) for _ in range(k)]
for point in points:
    for y in range(point[0], point[2]):
        for x in range(point[1], point[3]):
            array[x][y] += 1

dx, dy = [0,0,-1,1], [1,-1,0,0]

def bfs(array, a,b):
    q = deque([(a,b)])
    array[a][b] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx and nx < n and 0 <= ny and ny < m:
                if array[nx][ny] == 0:
                    array[nx][ny] = 'x'
                    count += 1
                    q.append((nx,ny))
    return count

answer = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            answer.append(bfs(array, i,j)) 

answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))