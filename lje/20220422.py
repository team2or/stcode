#해커랭크
#복습
#15 Days of Learning SQL
#https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true
#해석: https://yurimyurim.tistory.com/4
SELECT S.submission_date, H_Count.hacker_count, H_Best.hacker_id, H.name FROM Submissions S
-- 현재까지 매일 submission한 hackers
-- 해커별로 해당일자까지 중복을 제외한 제출 건수가
-- (해당일자-시작일자) 차이 일수와 같으면 계속 제출한 걸 알 수 있음
JOIN (SELECT submission_date, count(DISTINCT hacker_id) as hacker_count FROM Submissions S1 WHERE submission_date - DATE('2016-03-01') = (SELECT count(DISTINCT submission_date) FROM Submissions S2 WHERE S2.submission_date < S1.submission_date AND S2.hacker_id=S1.hacker_id) GROUP BY submission_date) H_Count ON S.submission_date=H_Count.submission_date
-- 날짜별로 가장 많이 제출한 hacker 구하기
-- 날짜, 해커아이디를 GROUP BY해서 제출 수 구하기
JOIN (SELECT submission_date, hacker_id FROM Submissions S3 WHERE hacker_id = (SELECT hacker_id FROM Submissions S4 WHERE S4.submission_date=S3.submission_date GROUP BY hacker_id ORDER BY count(submission_id) DESC, hacker_id limit 1) GROUP BY submission_date, hacker_id) H_Best ON S.submission_date=H_Best.submission_date
JOIN Hackers H ON H_Best.hacker_id=H.hacker_id
GROUP BY S.submission_date, H_Count.hacker_count
ORDER BY S.submission_date;

#다른 답안: https://ysyblog.tistory.com/208

#백준
#BFS
#소수 경로
#https://www.acmicpc.net/problem/1963
#답안:https://cijbest.tistory.com/13
from collections import deque
import math
#에라토스테네스의 체: https://freedeveloper.tistory.com/392
#체로 걸러내듯 소수만 남기는 알고리즘
def prime():
    prime_num = [True]*10001
    #2부터 n의 제곱근까지 모든 수를 확인
    for i in range(2, int(math.sqrt(10000))+1):
        #i가 소수일 경우
        if prime_num[i] == True:
            #i를 제외한 i의 모든 배수를 False처리
            j=2
            while i*j <= 10000:
                prime_num[i*j] = False
                j+=1
    return prime_num

#완전탐색같은 BFS로 각 자리수에 숫자를 바꿔가며 소수일 경우 카운트함
def bfs(start,end):
    q = deque([(start,0)])
    visited = [0 for _ in range(10000)]
    visited[start] = 1
    while q:
        now, cnt = q.popleft()
        if now == end:
            return cnt
        strNow=str(now)
        #각 자리에 0~9로 변경하면서 소수인지 확인
        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i]+str(j)+strNow[i+1:])
                if visited[temp] == 0 and primes[temp] and temp >=1000:
                    visited[temp] = 1
                    q.append((temp, cnt+1))
primes = prime()
t = int(input())
for _ in range(t):
    start,end = map(int, input().split())
    answer = bfs(start, end)
    if answer == None:
        print("Impossible")
    else:
        print(answer)


