# 프로그래머스_SQL
#이름이 없는 동물의 아이디
#https://programmers.co.kr/learn/courses/30/lessons/59039
#NAME-NULL이면 이름이 NULL인 경우를 찾음
#데이터가 없는 것을 찾고 싶다면 IS NULL 사용해야 함
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL ORDER BY ANIMAL_ID;

#이름이 있는 동물의 아이디
#https://programmers.co.kr/learn/courses/30/lessons/59407
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL ORDER BY ANIMAL_ID;

#백준
#도서관
#https://www.acmicpc.net/problem/1461
n, m = map(int, input().split())
p = list(map(int, input().split()))
minus = sorted([])
plus = sorted([], reverse=True)
max_din = abs(max(p))
for i in p:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

work = 0
for j in range(0, 5, 3):
    print(j)