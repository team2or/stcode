#해커랭크
#복습
#SQL Project Planning
#https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true
#답안: https://techblog-history-younghunjo1.tistory.com/170
SELECT Start_Date, min(End_Date) FROM (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) A, (SELECT End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) B
WHERE Start_Date < End_Date
GROUP BY Start_Date
ORDER BY DATEDIFF(min(End_Date), Start_Date), Start_Date;

#프로그래머스
#
#주차요금계산
#https://programmers.co.kr/learn/courses/30/lessons/92341
from datetime import datetime
import math
def dateToMinutes(date):
    h, m = map(int, date.split(':'))
    return h*60 + m
def solution(fees, records):
    parking = {}
    for re in records:
        t, n, l = map(str, re.split())
        if n not in parking:
            parking[n] = [dateToMinutes(t)]
        else:
            parking[n].append(dateToMinutes(t))

    answer = []
    for num, time in parking.items():
        cost = 0
        total_time = 0
        while time:
            f = time.pop(0)
            if len(time):
                s = time.pop(0)
            else:
                s = dateToMinutes("23:59")
            total_time += s-f
        if total_time-fees[0] > 0:
            cost += fees[1] + (math.ceil(((total_time-fees[0])/fees[2]))*fees[3])
        else:
            cost += fees[1]
        answer += [[num, int(cost)]]
    return [i[1] for i in sorted(answer)]

solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
solution([1, 461, 1, 10],["00:00 1234 IN"])

#참고
#무조건 반올림: math.ceil
#https://jsikim1.tistory.com/223
#시간을 분으로 변경하는 함수
#https://velog.io/@minnseong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%B0%A8-%EC%9A%94%EA%B8%88-%EA%B3%84%EC%82%B0
