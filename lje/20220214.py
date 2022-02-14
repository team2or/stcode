# 프로그래머스_SQL
#입양 시각 구하기(1)
#https://programmers.co.kr/learn/courses/30/lessons/59412
SELECT substring(DATETIME, 12, 2) "HOUR", COUNT(substring(DATETIME, 12, 2)) "COUNT" FROM ANIMAL_OUTS WHERE substring(DATETIME, 12, 2) > 8 AND substring(DATETIME, 12, 2) < 20 GROUP BY substring(DATETIME, 12, 2) ORDER BY substring(DATETIME, 12, 2);

#입양 시각 구하기(2)
#https://programmers.co.kr/learn/courses/30/lessons/59413

#WITH 재귀(RECURSIVE) 이용해야함 + JOIN
#https://hyunmin1906.tistory.com/149
WITH RECURSIVE h AS(
    SELECT 0 AS HOUR UNION ALL SELECT HOUR+1 FROM h WHERE HOUR < 23)
SELECT HOUR, COUNT(ANIMAL_ID) "COUNT" FROM h
LEFT JOIN ANIMAL_OUTS ON (HOUR = date_format(DATETIME, '%H')) GROUP BY HOUR;

#백준
#주유소
#https://www.acmicpc.net/problem/13305
n = int(input())
k = list(map(int, input().split()))
l = list(map(int, input().split()))

answer = k[0]*l[0]
min_l = l[0]
for i in range(1, n-1):
    if min_l > l[i]:
        min_l = l[i]
    answer += k[i]*min_l
print(answer)