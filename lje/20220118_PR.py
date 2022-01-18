#프로그래머스
#최소값과 최대값
#https://programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    s = list(map(int, s.split(' ')))
    min = 0
    max = 0
    for i in s:
        if min == 0 and max == 0:
            min = i
            max = i
        if min > i:
            min = i
        if max < i:
            max = i
    answer = f'({min} {max})'
    return answer

solution("1 2 3 4")
solution("-1 -2 -3 -4")
solution("-1 -1")

#다른 답
def solution(s):
    s = list(map(int, s.split(' ')))
    return str(min(s)) + ' ' + str(max(s))


#N개의 최소공배수
#https://programmers.co.kr/learn/courses/30/lessons/12953
import math
def solution(arr):
    lcm = arr[0]
    for i in arr[1:]:
        lcm = i*lcm // math.gcd(lcm, i)
    return lcm

solution([2,6,8,14])
solution([1,2,3])

#최대공약수 함수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

#최소공배수 함수
def lcm(a,b):
    return a*b // gcd(a, b)

def solution(arr):
    _lcm = arr[0]
    for i in arr[1:]:
        _lcm = lcm(_lcm,i)
    return _lcm

solution([2,6,8,14])