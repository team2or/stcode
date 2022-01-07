# https://programmers.co.kr/learn/courses/30/lessons/12932
# Programmers 19232.

def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n), 0, -1):
        answer.append(int(n[i-1]))
    return answer
