#해커랭크
#복습
#print prime numbers
#https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true
#2~1000까지 숫자 출력/information_schema.tables로 가상테이블 설정
SET @prime = 1;
SELECT * FROM (SELECT @prime := @prime+1 AS PRIME FROM information_schema.tables t1, information_schema.tables t2 LIMIT 1000) list_primes;

#prime과 div의 값이 동일하지 않을때(PRIME != DIVISOR) 두 수를 나눈 나머지(MOD)가 0인 수를 제외하여 출력
SET @prime = 1;
SET @div = 1;
SELECT * FROM (SELECT @prime := @prime+1 AS PRIME FROM information_schema.tables t1, information_schema.tables t2 LIMIT 1000) list_primes WHERE NOT EXISTS(SELECT * FROM (SELECT @div := @div+1 AS DIVISOR FROM information_schema.tables t1, information_schema.tables t2 LIMIT 1000) list_divs WHERE MOD(PRIME, DIVISOR)=0 AND PRIME != DIVISOR);

#GROUP_CONCAT으로 한줄출력, SEPARATOR로 구분자 설정
SET @prime = 1;
SET @div = 1;
SELECT group_concat(PRIME SEPARATOR '&') FROM (SELECT @prime := @prime+1 AS PRIME FROM information_schema.tables t1, information_schema.tables t2 LIMIT 1000) list_primes WHERE NOT EXISTS(SELECT * FROM (SELECT @div := @div+1 AS DIVISOR FROM information_schema.tables t1, information_schema.tables t2 LIMIT 1000) list_divs WHERE MOD(PRIME, DIVISOR)=0 AND PRIME != DIVISOR);

#백준
#BFS
#결혼식
#https://www.acmicpc.net/problem/5567
#답안:https://fre2-dom.tistory.com/129
from collections import deque
n = int(input())
m = int(input())
visited = [0 for i in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
print(graph)
def bfs(x):
    q = deque([x])
    cnt = 0

    visited[x] = 1
    while q:
        friend = q.popleft()
        cnt += 1
        for i in graph[friend]:
            if visited[i] == 0:
                visited[i] = visited[friend]+1
                q.append(i)
bfs(1)
print(visited.count(2)+visited.count(3))