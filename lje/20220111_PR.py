#프로그래머스
#문자열을 정수로 바꾸기
#https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    answer = int(s)
    
    return answer

#탐욕법(Greedy) 체육복
#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
            lost.remove(i)
    for i in lost:
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
    return answer

solution(5,[2,4],[1,3,5])
solution(5,[2,4],[3])
solution(3,[3],[1])
solution(2,[1,2],[1])
solution(20,[3,7,6,5,10,15,13,20],[3,4,2,8,13,14,19])
solution(3,[1,2],[2,3])
solution(2,[2],[1])

#답안적용
#차집합으로 서로 중복되는 숫자 제거
def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i-1)
        elif i + 1 in lost_set:
            lost_set.remove(i+1)
    answer = n - len(lost_set)   
    return answer