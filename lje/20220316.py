#해커랭크
#African Cities
#https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true
from ast import Num

from torch import HalfTensor


SELECT CITY.Name FROM CITY LEFT JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code WHERE COUNTRY.Continent = 'Africa';

#Draw The Triangle 2
#https://www.hackerrank.com/challenges/draw-the-triangle-2/problem?isFullScreen=true
#'* ' 출력때 뒤에 공백 없으면 실패로 뜸
SET @NUMBER = 0;
SELECT REPEAT('* ', @NUMBER := @NUMBER +1) FROM information_schema.tables LIMIT 20;

#[참고]
#https://velog.io/@nightnova96/SQLHackerRank-Draw-The-Triangle-12

#백준
#완전탐색
#백설공주와 일곱 난쟁이
#https://www.acmicpc.net/problem/3040
hat_num = []
num_count = 0
for i in range(9):
    num = int(input())
    if num_count < 100:
        num_count += num
        hat_num.append(num)
    elif num_count == 100 and len(hat_num) == 7:
        break
    else:
        if (num_count-100) in hat_num:
            hat_num.remove(num_count-100)
        else:
            num_count += num
            hat_num.append(num)

print(hat_num)
print(num_count)     
for hat in hat_num:
    print(hat)


#다른 답안
import itertools

hat_num = []
for i in range(9):
    hat_num.append(int(input()))

hats = list(itertools.combinations(hat_num,7))
for i in hats:
    if sum(i) == 100:
        for j in i:
            print(j)
        break
    
#[참고]
#브루트포스 알고리즘
#itertools를 이용하여 모든 조합이나 순열을 얻을 수 있음
#https://velog.io/@supergangho/2-Python-%EC%A1%B0%ED%95%A9-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4

