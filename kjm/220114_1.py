# https://programmers.co.kr/learn/courses/30/lessons/42748
# Programmers 42748.

def solution(array, commands):
    answer = []
    for n in commands:
        i, j, k = n
        array1 = array[i-1:j]
        array1.sort()
        answer.append(array1[k-1])
    
    return answer