#해커랭크
#Japan Population
#https://www.hackerrank.com/challenges/japan-population/problem?isFullScreen=true
SELECT sum(population) FROM CITY WHERE countrycode = 'JPN';

#Top Earners
#https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true
#GROUP BY로 묶어 표현, ORDER BY로 내림차순으로 해서 큰값이 먼저 출력되게 함.
#LIMIT로 최대값 출력
SELECT salary*months, count(*) FROM Employee GROUP BY salary*months ORDER BY salary*months DESC LIMIT 1;

#[참고]
#https://jogrammer.tistory.com/181

#백준
#완전탐색/다이나믹프로그래밍(DP)
#1, 2, 3 더하기
#https://www.acmicpc.net/problem/9095

#답안1
#https://devvvyang.tistory.com/17
T = int(input())
d = [1,2,4]
for i in range(4,12):
    d.append(d[i-2]+d[i-3]+d[i-4])

for _ in range(T):
    n = int(input())
    print(d[n-1])

#답안2
#https://tooo1.tistory.com/112
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return f(n-1) + f(n-2) + f(n-3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(f(n))