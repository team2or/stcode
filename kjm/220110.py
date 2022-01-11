# https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3
# Programmers 86051.

def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            print(i)
            answer += i
        
    return answer


solution([1, 2, 3, 4, 6, 7, 8, 0])