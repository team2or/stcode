# https://programmers.co.kr/learn/courses/30/lessons/12953
# Programmers 12953.

# 1) lmc import 불가
from math import lcm

def solution(arr):    
    answer = arr[0]
    for i in range(len(arr)):
        answer = lcm(answer, arr[i])
    return answer

# 2)
from math import gcd

def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = (n*answer) // gcd(n,answer)
    return answer