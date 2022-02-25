#해커링크
#Revising the Select Query II(쿼리 선택 수정II)
#https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true
SELECT NAME FROM CITY WHERE CountryCode = 'USA' AND  population >= 120000;

#Weather Observation Station 5(기상관측소5)
#https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
#한번에 출력하는 방법은 따로 없는 듯 하다.
SELECT CITY, length(CITY) FROM STATION ORDER BY length(CITY), CITY LIMIT 1;
SELECT CITY, length(CITY) FROM STATION ORDER BY length(CITY) DESC, CITY LIMIT 1;

#백준
#컵홀더
#https://www.acmicpc.net/problem/2810
n = int(input())
seat = input()
seat = list(seat)
answer = ''
while len(seat) > 1:
    f = seat.pop(0)
    s = seat.pop(0)
    if f != s:
        answer += f'{f}*'
        seat.insert(0, s)
    else:
        if f == 'S' and s == 'S':
            answer += f'{f}*'
            seat.insert(0, s)
        else:
            answer += f'{f+s}*'
if len(seat) == 1:
    answer = f'*{answer+seat[0]}*'
else:
    answer = f'*{answer}'

if answer.count('*') > n:
    print(n)
else:
    print(answer.count('*'))