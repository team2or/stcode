#해커랭크
#Select By ID
#https://www.hackerrank.com/challenges/select-by-id/problem?isFullScreen=true
SELECT * FROM CITY WHERE ID = 1661;

#Challenges
#https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
#4번째 조건 놓침(문제를 제대로 읽자)
SELECT C.hacker_id, H.name, count(C.hacker_id) as challenges_created FROM Challenges C LEFT JOIN Hackers H ON C.hacker_id = H.hacker_id
GROUP BY C.hacker_id, H.name ORDER BY challenges_created DESC, C.hacker_id;

#만약 2명 이상이 똑같은 문제 개수를 만들었을 때, 그 문제 개수가 문제 개수의 최댓값보다 작다면 그 때의 학생들은 출력시키지 않아야 함(최댓값이 여러명이면 그 학생들은 모두 출력 / 최댓값보다 작으면 출력x)
#[참고]
#https://techblog-history-younghunjo1.tistory.com/157
SELECT C.hacker_id, H.name, count(C.hacker_id) as challenges_created FROM Challenges C LEFT JOIN Hackers H ON C.hacker_id = H.hacker_id GROUP BY C.hacker_id, H.name
HAVING challenges_created IN (SELECT sub1.challenges_created FROM (SELECT count(*) as challenges_created FROM Challenges GROUP BY hacker_id) sub1  GROUP BY sub1.challenges_created HAVING count(*) = 1)
OR challenges_created = (SELECT max(sub2.challenges_max) FROM (SELECT count(hacker_id) as challenges_max FROM Challenges GROUP BY hacker_id) sub2) ORDER BY challenges_created DESC, C.hacker_id;

#WHERE / HAVING 차이
#https://velog.io/@ljs7463/SQL-having-%EA%B3%BC-where-%EC%B0%A8%EC%9D%B4

#max(count)하는 법
#https://okky.kr/article/585386


#백준
#DFS/BFS
#순열 사이클
#https://www.acmicpc.net/problem/10451
from collections import deque

t = int(input())

def bfs(v):
    q = deque([v])
    c = 0
    while q:
        x = q.popleft()
        if not visited[x]:
            visited[x] = 1
            c += 1
            for i in graph[x]:
                q.append(i)
    return c

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    sort_array = sorted(array)
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    for i in range(n):
        graph[array[i]].append(sort_array[i])
        graph[sort_array[i]].append(array[i])
    count = 0
    for i in range(1,n+1):
        c = bfs(i)
        if c > 0:
            count += 1
    print(count)

#다른 답안
#DFS사용
#https://jinu0418.tistory.com/102
t = int(input())

for _ in range(t):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [1] + [0] * n
    count = 0
    for i in range(1,n+1):
        stack = [i]
        if visited[i] == 0:
            count += 1
            visited[i] = 1
        while stack:
            x = stack.pop()
            c = nums[x]
            if visited[c] == 0:
                visited[c] = 1
                stack.append(c)