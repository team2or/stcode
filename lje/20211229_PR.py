#프로그래머스

#문제1
#최대공약수와 최소 공배수
#https://programmers.co.kr/learn/courses/30/lessons/12940

import math
def solution(n, m):
    g = math.gcd(n,m)
    l = int(n*m / g)
    answer = [g,l]
    return answer

solution(3,12)
solution(2,5)

#문제2
#모의고사
#https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    f = [1,2,3,4,5]
    s = [2,1,2,3,2,4,2,5]
    t = [3,3,1,1,2,2,4,4,5,5]
    #점수 리스트로 만들기
    score = [0,0,0]
    answer=[]
    for i in range(len(answers)):
        fd = i%5
        sd = i%8
        td = i%10
        if answers[i] == f[fd]:
            score[0] += 1
        if answers[i] == s[sd]:
            score[1] += 1
        if answers[i] == t[td]:
            score[2] += 1
    print(score)
    for i, v in enumerate(score):
        #리스트에서 최대값 찾기 max()함수 이용
        if v == max(score):
            answer.append(i+1)
    return sorted(answer)
    
solution([1,2,3,4,5])
solution([1,3,2,4,2])
