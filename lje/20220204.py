#백준
#30
#https://www.acmicpc.net/problem/10610
n = input()
n = ''.join(sorted(n, reverse=True))
if int(n)%30 == 0:
    print(n)
else:
    print(-1)
#프로그래머스_MySQL
#모든 레코드 조회하기
#https://programmers.co.kr/learn/courses/30/lessons/59405
SELECT * FROM ANIMAL_INS;

#상위 n개 레코드
#https://programmers.co.kr/learn/courses/30/lessons/59405
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;

