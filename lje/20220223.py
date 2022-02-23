#해커링크
#Weather Observation Station 1(기상관측소1)
#https://www.hackerrank.com/challenges/weather-observation-station-1/problem?isFullScreen=true3
SELECT CITY, STATE FROM STATION;



#Weather Observation Station 3(기상관측소3)
#https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE MOD(ID,2) = 0;

#[참고]
#중복제거
#https://velog.io/@kimju0913/SQL-%EC%A4%91%EB%B3%B5%EC%A0%9C%EA%B1%B0-DISTINCT-GROUP-BY
#몫과 나머지
#https://hyunie-y.tistory.com/13

#프로그래머스
#카펫
#https://programmers.co.kr/learn/courses/30/lessons/42842

#답안
#https://coblin.xyz/35
def solution(brown, yellow):

    tot = brown + yellow

    for width in range(tot, 2, -1):
        if tot/width == 0:
            length = tot//width
            if yellow == (width-2)*(length-2):
                return [width, length]