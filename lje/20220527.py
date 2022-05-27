#해커랭크
#복습
#Type of Triangle
#https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true
#조건의 순서가 중요 위에서 먼저 적용되는 조건이면 아래조건도 만족해도 위에 조건으로 적용됨
SELECT CASE WHEN A=B AND B=C THEN "Equilateral"
WHEN A>=B+C OR B>=A+C OR C>=A+B THEN "Not A Triangle"
WHEN A=B OR A=C OR B=C THEN "Isosceles"
ELSE "Scalene" END FROM TRIANGLES;


#프로그래머스
#피보나치 수
#https://programmers.co.kr/learn/courses/30/lessons/12945
n = 3
n=5
cnt = n
p_list = [0,1]
while cnt > 0:
    p_list.append(p_list[-1]+p_list[-2])
    cnt -=1
print(p_list[n]%1234567)