# https://programmers.co.kr/learn/courses/30/lessons/42862
# Programmers 42862.

def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for i in range(1, n+1):
        if i not in lost:
            answer += 1
        else:
            if i in reserve:
                answer += 1
                reserve.remove(i)
                lost.remove(i)
    for i in lost:
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)
    return answer