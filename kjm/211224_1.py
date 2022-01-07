# https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
# Programmers 12915.

def solution(s, n):
    return sorted(s, key = lambda x : (x[n],x)) 
