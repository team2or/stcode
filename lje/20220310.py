#해커링크
#Weather Observation Station 12
#https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION  WHERE CITY REGEXP "^[^aeiou]" AND CITY REGEXP "[^aeiou]$";

#Revising Aggregations - The Count Function
#https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem?isFullScreen=true
SELECT count(ID) FROM CITY WHERE POPULATION >= 100000;

#프로그래머스
#스택/큐
#프린터
#https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    pr = []
    for k, v in enumerate(priorities):
        pr.append([k,v])
    answer = []
    while len(pr):
        m = max(priorities)
        prior = priorities.pop(0)
        p = pr.pop(0)
        if m != p[1]:
            priorities.append(prior)
            pr.append(p)
        else:
            answer.append(p[0])

    return answer.index(location) +1

solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)

#다른답안
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        #any() 조건 중 하나라도 만족하면 true
        #다만 리스트 값이 많을 수록 비효율적
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer