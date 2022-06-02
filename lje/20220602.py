#해커랭크
#복습
#Average Population of Each Continent
#https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true
SELECT COUNTRY.Continent, floor(avg(CITY.Population)) FROM CITY JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code GROUP BY COUNTRY.Continent;

#프로그래머스
#최솟값 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12941
A = [1,4,2]
B = [5,4,4]
A = [1,2]
B = [3,4]
A = sorted(A)
B = sorted(B, reverse=True)
answer = 0
for a, b in zip(A, B):
    answer += a * b
print(answer)