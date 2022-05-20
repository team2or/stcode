#거꾸로 구구단 

import sys


def solution(s):
    if s[0] == ")" or s[-1]=="(":
        return False
    for i in s:
        answer = []
        if i =="(":
            answer.append(i)
        else:
            if len(answer) ==0:
                False
            else:
                answer.pop()
    return answer==[]

if __name__=="__main__":
    hats=solution('(())')
    print(hats)
