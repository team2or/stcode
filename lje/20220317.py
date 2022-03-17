#해커랭크
#Weather Observation Station 13
#https://www.hackerrank.com/challenges/weather-observation-station-13/problem?isFullScreen=true
SELECT round(sum(LAT_N), 4) FROM STATION WHERE LAT_N > 38.7880 and LAT_N < 137.2345;

#The Blunder
#https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true
#round: 일반적인 반올림 기준
#ceil: 소수점 이하 올림(값보다 큰 정수 중 가장 작은 정수를 가져옴)
#ex) ceil(10.1) -> 11
#replace로 0을 공백으로 변경
SELECT ceil(avg(Salary)-avg(replace(Salary, 0, ''))) FROM EMPLOYEES;

#[참고]
#https://jjeongil.tistory.com/928

#백준
#완전탐색
#호텔 방 번호
#https://www.acmicpc.net/problem/5671
#입력은 여러 개의 테스트 케이스로 이루어져 있고(몇개인지 모르기 때문에 while로 반복문 돌림)
#테스트 케이스가 없을 때 while문 종료 시켜야 함.
while 1:
    try:
        n, m = map(int, input().split())
    except:
        break
    count = (m+1) - n
    for i in range(n,m+1):
        room_num = list(str(i))
        while room_num:
            num = room_num.pop(0)
            if num in room_num:
                count -= 1
                break
    print(count)

#다른 답안
#https://devlibrary00108.tistory.com/467
#set()으로 중복숫자 검증한 후 원래 방번호와 비교
#set()한 숫자와 원래 방번호 숫자가 같으면 + 1
import sys
input = sys.stdin.readline

while 1:
    try:
        N, M = map(int, input().split())
    except:
        break
    ans = 0
    for num in range(N,M+1):
        cnt = set()
        s_num = str(num)
        for char in s_num:
            cnt.add(char)
        if len(s_num) == len(cnt):
            ans += 1
    print(ans)