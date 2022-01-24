# https://programmers.co.kr/learn/courses/30/lessons/64065
# Programmers 64065.

import re
 
def solution(s):
    answer = []
    a = s.split(',{')
    a.sort(key = len)
    for j in a:
        numbers = re.findall("\d+", j)
        for k in numbers:
            if int(k) not in answer:
                answer.append(int(k))
    return answer