#해커랭크
#복습
#Top Earners
SELECT concat(max(salary*months), "  ", count(salary*months))  FROM Employee GROUP BY salary*months ORDER BY salary*months DESC LIMIT 1;

#프로그래머스
#복습
#스택/큐
#다리를 지나는 트럭
#https://programmers.co.kr/learn/courses/30/lessons/42583
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
bridge = [0]*bridge_length
time = 0
while bridge:
    time += 1
    bridge.pop(0)
    if truck_weights:
        if sum(bridge)+truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
print(time)


#이전 답안
def solution(bridge_length, weight, truck_weights):
    answer = 0
    while truck_weights:
        w = weight
        count = 0
        while w > 0:
            if count != 0:
                if len(truck_weights) > 0 and w >= truck_weights[0]:
                    w -= truck_weights.pop(0)
                    answer += 1
                else:
                    break
            else:
                if len(truck_weights) > 0 and w >= truck_weights[0]:
                    w -= truck_weights.pop(0)
                    answer += 2
                    count += 1
                else:
                    break
    answer += bridge_length
    return answer - 1

