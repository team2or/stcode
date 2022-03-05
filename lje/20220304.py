#해커링크
#Weather Observation Station 11
#https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP "^[^aeiou]" OR CITY REGEXP "[^aeiou]$";

#Employee Names
#https://www.hackerrank.com/challenges/name-of-employees/problem?isFullScreen=true
SELECT name FROM Employee ORDER BY name;

#프로그래머스
#스택/큐
#기능개발
#https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

def solution(progresses, speeds):

    #각 과정이 완성되는 날짜 구하기
    complete = []
    while len(progresses):
        prog = progresses.pop(0)
        speed = speeds.pop(0)
        count = 0
        while prog < 100:
            prog += speed
            count += 1
        complete.append(count)

    #서비스가 배포될 개수 구하기
    answer = []
    num = 1
    while len(complete) > 1:
        fs = complete.pop(0)
        sc = complete.pop(0)
        if fs >= sc:
            num += 1
            if len(complete) != 0:
                complete.insert(0, fs)
            else:
                answer.append(num)
        else:
            answer.append(num)
            complete.insert(0, sc)
            num = 1
    if len(complete) == 1:
        answer.append(1)

    return answer

#다른 답안
import math;

def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        #math.ceil 소수점 올림하여 정수로 반환
        days.append(math.ceil((100-progresses[i])/speeds[i]))

    temp = days[0]
    cnt = 0 #cnt = 0인 이유는 for문 맨 처음이 동일한 값임
    for day in days:
        if day <= temp:
            cnt+=1
        else:
            answer.append(cnt)
            cnt = 1
            temp = day
    answer.append(cnt)
    return answer

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])