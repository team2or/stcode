# 프로그래머스_SQL
# 최대값 구하기
# https://programmers.co.kr/learn/courses/30/lessons/59415
SELECT MAX(DATETIME) as "시간" FROM ANIMAL_INS

# 최솟값 구하기
# https://programmers.co.kr/learn/courses/30/lessons/59038
SELECT MIN(DATETIME) as "시간" FROM ANIMAL_INS

# 백준
# 기타줄
# https://www.acmicpc.net/problem/1049
n, m = map(int, input().split())
a = []
l = []
for _ in range(m):
    f, s = map(int, input().split())
    a.append(f)
    l.append(s)

answer = 0
while n > 0:
    if n < 6:
        if min(l)*n <= min(a):
            answer += min(l)*n
            n = 0
        else:
            answer += min(a)
            n = 0
    else:
        if min(l)*6 <= min(a):
            answer += min(l)*6
            n -= 6
        else:
            answer += min(a)
            n -= 6
print(answer)
