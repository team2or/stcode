# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
# Programers 12917.

def solution(s):
    list_ = list(s)
    list_.sort(reverse=True)
    answer = ""
    for j in list_:
        answer += j
    return answer