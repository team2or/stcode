#해커링크
#Weather Observation Station 8(기상관측소8)
#https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true
SELECT CITY FROM STATION WHERE SUBSTR(CITY, 1, 1) IN ('a', 'e', 'i', 'o', 'u') AND SUBSTR(CITY, -1, 1) IN ('a', 'e', 'i', 'o', 'u');

#다른 답안
SELECT CITY FROM STATION WHERE CITY REGEXP "^[aeiou]" AND CITY REGEXP "[aeiou]$";

#Weather Observation Station 9(기상관측소9)
#https://www.hackerrank.com/challenges/weather-observation-station-9/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP "^[^aeiou]";

#[참고]
#정규식
#https://yurimkoo.github.io/analytics/2019/10/26/regular_expression.html

#프로그래머스
#완전탐색
#소수찾기
#https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations

def solution(numbers):
    #문자열 리스트로 하나씩 나눔
    numbers = list(numbers)
    array = []
    #리스트에 담긴 숫자를 1~len(numbers) 자리수까지 모든 조합 구하기
    for i in range(1, len(numbers)+1):
        com = permutations(numbers, i)
        array += [int(''.join(c)) for c in com]

    answer = 0
    #set으로 동일한 숫자 지운 후 소수판별하기
    for n in set(array):
        result = 0
        for i in range(1, n+1):
            if n%i == 0 and n != 0:
                result += 1
            #소수는 1과 자기자신만 있으므로
            #3이상일 경우는 소수 아님
            if result >= 3:
                break

        if result == 2:
            answer += 1
    return answer
solution("1231")

#[참고]
#https://dev-jinee.tistory.com/7