#해커링크
#Type of Triangle
#https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true
#CASE문: https://info-lab.tistory.com/305
#조건연산자(!= or <>): https://zorba91.tistory.com/32
SELECT
    CASE 
        WHEN A=B AND B=C THEN 'Equilateral'
        WHEN A + B <= C THEN 'Not A Triangle'
        WHEN A!=B AND A!=C AND B!=C THEN 'Scalene'
        ELSE 'Isosceles'
    END
FROM TRIANGLES;

#Weather Observation Station 2
#https://www.hackerrank.com/challenges/weather-observation-station-2/problem?isFullScreen=true
SELECT round(sum(LAT_N), 2) lat, round(sum(LONG_W), 2) lon FROM STATION;

#백준
#해시 알고리즘
#IOIOI
#https://www.acmicpc.net/problem/5525

#시간초과
n = int(input())
m = int(input())
s = input()
s = list(s)
p = 'IOI' + 'OI'*(n-1)
count = 0
line = s[:len(p)]
del s[:len(p)]
while len(s):
    if line == list(p):
        count += 1
        del line[0]
        line.append(s.pop(0))
    else:
        del line[0]
        line.append(s.pop(0))
print(count)

#답안
#https://velog.io/@woga1999/BOJ-5525%EB%B2%88-IOIOI-Python
N = int(input())
M = int(input())
S = input()

cnt = 0
pattern = 0
i = 1

while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        pattern += 1
        if pattern == N:
            pattern -= 1
            cnt += 1
        i += 1
    else:
        pattern = 0
    i += 1
print(cnt)



