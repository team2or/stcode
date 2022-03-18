#해커랭크
#Weather Observation Station 14
#https://www.hackerrank.com/challenges/weather-observation-station-14/problem?isFullScreen=true
from cgitb import reset


SELECT max(truncate(LAT_N,4)) FROM STATION WHERE LAT_N < 137.2345;

#Average Population of Each Continent
#https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true
#LEFT조인을 하면 NULL 값이 나옴. INNER 조인으로 둘 다 해당하는 교집합을 해야 함
SELECT COUNTRY.Continent, floor(avg(CITY.POPULATION)) FROM CITY INNER JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code GROUP BY COUNTRY.Continent;

#백준
#완전탐색
#거꾸로 구구단
#https://www.acmicpc.net/problem/13410
n, k = map(int, input().split())
result = []
for i in range(1,k+1):
    mul = str(n*i)
    if len(mul) == 1:
        result.append(int(mul))
    else:
        mul_list = list(mul)
        mul_result = ''
        while mul_list:
            mul_result += mul_list.pop()
        result.append(int(mul_result))
print(max(result))

#다른 답안
N, K = map(int, input().split())
#array를 [::-1]으로 설정해서 역순으로 정렬함. 
li = [int(str(N*i)[::-1]) for i in range(1, K+1)]
print(max(li))