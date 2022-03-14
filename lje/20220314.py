#해커링크
#Revising Aggregations - Averages
#https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true
from pyrsistent import T


SELECT avg(POPULATION) FROM CITY WHERE DISTRICT = "California";

#Population Census
#https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true
#조인문제: population을 구하는 문제 이므로 left join이용함.
SELECT sum(CITY.population) FROM CITY LEFT JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code WHERE COUNTRY.CONTINENT = 'Asia';

#프로그래머스
#다리를 지나는 트럭
#https://programmers.co.kr/learn/courses/30/lessons/42583
#실패
def solution(bridge_length, weight, truck_weights):
    answer = 0
    while truck_weights:
        w = weight
        if answer != 0:
            answer += bridge_length -1
        else:
            answer += bridge_length
        while w > 0:
            if len(truck_weights) > 0 and w >= truck_weights[0]:
                w -= truck_weights.pop(0)
                answer += 1
            else:
                break

    return answer

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])

#답안
#https://js-note.tistory.com/52
def solution(bridge_length, weight, truck_weights):
    answer = 0
    #bridge_length만큼 q 리스트 생성
    q = [0] * bridge_length
    while truck_weights:
        q.pop(0)
        #q에 원소 하나씩 뺄때마다 1초씩 증가 됨
        answer += 1
        #다리 위의 트럭의 합계와 다음 트럭의 합계가 
        #weight보다 작으면 다음 트럭 통과시키기
        if sum(q) + truck_weights[0] <= weight:
            q.append(truck_weights.pop(0))
        #weight보다 크면 다리 위에 있는 트럭 0으로 밀어내기
        else:
            q.append(0)
    answer += bridge_length
    return answer

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])