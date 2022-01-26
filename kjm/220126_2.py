# https://programmers.co.kr/learn/courses/30/lessons/86491
# Programmers 86491.

def solution(sizes):
    width, hight = [], []
    for i in sizes:
        width.append(max(i))
        hight.append(min(i))
    answer = max(width) * max(hight)
    return answer

# Example
'''
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
'''