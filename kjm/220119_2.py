# https://programmers.co.kr/learn/courses/30/lessons/12903
# Programmers 12903.

def solution(s):
    if len(s)%2 == 0:
        answer = s[(len(s)//2)-1:(len(s)//2)+1]
    else:
        answer = s[len(s)//2]
    
    return answer