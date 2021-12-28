def solution(s, n):
    return sorted(s, key = lambda x : (x[n],x)) 