# https://programmers.co.kr/learn/courses/30/lessons/12918
# Programmers 12918

def solution(s):
    if len(s) == 4 or len(s) == 6:
        answer = s.isdigit()
    else:
        answer = False
    return answer