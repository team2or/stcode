#프로그래머스_SQL
#입양시각구하기(2)
#https://programmers.co.kr/learn/courses/30/lessons/59413
#UNION: https://sesok808.tistory.com/510
#WITH RECURSIVE: https://sas-study.tistory.com/165
WITH RECURSIVE hour AS (SELECT 0 AS h UNION ALL SELECT h+1 FROM hour WHERE h < 23)
SELECT hour.h, count(ANIMAL_OUTS.DATETIME) FROM hour LEFT JOIN ANIMAL_OUTS ON hour.h = hour(ANIMAL_OUTS.DATETIME) GROUP BY h;


#백준
#스택
#제로
#https://www.acmicpc.net/problem/10773
#sys 사용해야 함. input()사용시 시간초과 뜸
import sys
k = int(sys.stdin.readline())
answer = []
for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0 and len(answer) > 0:
        answer.pop()
    else:
        answer.append(num)
print(sum(answer))