#해커랭크
#복습
#The PADS
#https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
SELECT CONCAT(Name, CONCAT('(', substr(Occupation, 1, 1), ')')) FROM OCCUPATIONS ORDER BY Name;
SELECT CONCAT('There are a total of ', count(*), ' ', lower(Occupation), 's.') FROM OCCUPATIONS GROUP BY Occupation ORDER BY count(*);

#새문제
#New Companies
#https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
#중복인 레코드가 존재한다 해서 DISTINCT로 중복제거
#JOIN으로 모든 테이블 조인
SELECT C.company_code, C.founder, count(DISTINCT L.lead_manager_code),
count(DISTINCT S.senior_manager_code), count(DISTINCT M.manager_code),
count(DISTINCT E.employee_code)
FROM Company C
JOIN Lead_Manager L ON C.company_code = L.company_code
JOIN Senior_Manager S ON C.company_code = S.company_code
JOIN Manager M ON C.company_code = M.company_code
JOIN Employee E ON C.company_code = E.company_code
GROUP BY C.company_code, C.founder
ORDER BY C.company_code;

#다른답안
#SELECT문으로 풂
select a.company_code, a.founder,
(select count(distinct lead_manager_code) from lead_manager where company_code = a.company_code),
(select count(distinct senior_manager_code) from senior_manager where company_code = a.company_code),
(select count(distinct manager_code) from manager where company_code = a.company_code),
(select count(distinct employee_code) from employee where company_code = a.company_code)
from company a
order by a.company_code asc;

#백준
#BFS
#미로탐색
#https://www.acmicpc.net/problem/2178
#백준 토마토와 비슷한 풀이방법

from collections import deque

n, m = map(int, input().split())
array = [list(map(int, ' '.join(input().split()))) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque([(0,0)])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = dx[i]+x, dy[i]+y
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                q.append((nx,ny))

print(array[n-1][m-1])

#[참고]
#https://devyuseon.github.io/boj/boj-2178/