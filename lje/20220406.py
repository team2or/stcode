#해커랭크
#복습
#Ollivander's Inventory
#https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
#age,power가 같은 지팡이 중에 가격이 젤 낮은 지팡이 찾기
SELECT W.id, P.age, W.coins_needed, W.power
FROM Wands W
 INNER JOIN Wands_Property P ON W.code = P.code
WHERE W.coins_needed = (SELECT MIN(W1.coins_needed)
                      FROM Wands W1
                       INNER JOIN Wands_Property P1 ON W1.code = P1.code
                      WHERE P1.is_evil = 0 
                      AND W1.power = W.power
                      AND P1.age = P.age)
ORDER BY W.power DESC, P.age DESC

#다른 답안
#https://bbeomgeun.tistory.com/66
SELECT w.ID, P.AGE, m.coins_needed, w.power from (SELECT code, min(coins_needed) as coins_needed, power from wands group by code, power) as m inner join wands as w on w.code = m.code and w.power = m.power and w.coins_needed = m.coins_needed inner join wands_property as p on p.code = w.code where p.is_evil = 0 order by w.power desc, p.age desc;


#새문제
#Symmetric Pairs
#https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true
#답안
#https://93nss.tistory.com/27
SELECT f1.X, f1.Y FROM Functions f1
INNER JOIN Functions f2 ON f1.X=f2.Y AND f1.Y=f2.X
 
GROUP BY f1.X, f1.Y
HAVING COUNT(f1.X)>1 or f1.X<f1.Y
 
ORDER BY f1.X;

#백준
#BFS
#단지번호붙이기
#https://www.acmicpc.net/problem/2667
array = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

from collections import deque
n = int(input())
array = [list(map(int, ' '.join(input().split()))) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(n, array,a,b):
    q = deque([(a,b)])
    array[a][b] = 0
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if array[nx][ny] == 1:
                    array[nx][ny] = 0
                    count += 1
                    q.append((nx,ny))
    return count

answer = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            answer.append(bfs(n,array,i,j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)