#해커랭크
#복습
#Placements
#https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
from multiprocessing.connection import answer_challenge
from selectors import EpollSelector


SELECT tab1.Name FROM (SELECT S.ID, S.Name, P.Salary FROM Students S LEFT JOIN Packages P ON S.ID = P.ID) AS tab1 LEFT JOIN (SELECT F.ID, P.Salary FROM Friends F LEFT JOIN Packages P ON F.Friend_ID = P.ID) AS tab2 ON tab1.ID = tab2.ID WHERE tab1.Salary < tab2.Salary ORDER BY tab2.Salary;

#새문제
#Occupations
#https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
SELECT
    max(CASE WHEN Occupation = 'Doctor' THEN Name END) 'Doctor',
    max(CASE WHEN Occupation = 'Professor' THEN Name END) 'Professor',
    max(CASE WHEN Occupation = 'Singer' THEN Name END) 'Singer',
    max(CASE WHEN Occupation = 'Actor' THEN Name END) 'Actor'
FROM (
  SELECT *, row_number() OVER (PARTITION BY Occupation ORDER BY Name) rn
  FROM OCCUPATIONS
) t
GROUP BY rn


#백준
#해시
#패션왕 신해빈
#https://www.acmicpc.net/problem/9375
t = int(input())
for i in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        f, s = map(str, input().split())
        if s in clothes:
            clothes[s] += [f]
        else:
            clothes[s] = [f]

    answer = 1
    for cloth in clothes.keys():
        # +1: 입지 않는 경우도 포함해야 하므로
        answer = answer * (len(clothes[cloth]) + 1) 

    #-1:아이템을 아무것도 안입는 경우는 빼야함
    print(answer-1)

#비슷한문제
#프로그래머스
#위장
#https://programmers.co.kr/learn/courses/30/lessons/42578