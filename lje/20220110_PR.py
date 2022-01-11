#프로그래머스
#없는 숫자 더하기
#https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(n):
    answer = 0
    for i in range(10):
        if i not in n:
            answer += i
        else:
            pass
    return answer

solution([1,2,3,4,6,7,8,0])
