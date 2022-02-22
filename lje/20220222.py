#프로그래머스_SQL
#오랜 기간 보호한 동물(1)
#https://programmers.co.kr/learn/courses/30/lessons/59044
SELECT A.NAME, A.DATETIME FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME IS NULL ORDER BY A.DATETIME LIMIT 3;

#보호소에서 중성화한 동물
#https://programmers.co.kr/learn/courses/30/lessons/59045
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.SEX_UPON_INTAKE LIKE "%Intact%" AND A.SEX_UPON_OUTCOME NOT LIKE "%Intact%";

#백준
#이장님 초대
#https://www.acmicpc.net/problem/9237
n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)

for i in range(n):
    t[i] += i+1
print(max(t)+1)