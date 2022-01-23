#프로그래머스
#문자열 내림차순으로 배치하기
#https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    l = [i for i in s]
    l.sort(reverse=True)
    return ''.join(l)

solution("Zbcdefg")

#이전 답
def solution(s):
    l = []
    answer = ""
    for i in s:
        l.append(i)
        l.sort(reverse=True)
    for j in l:
        answer += j
    return answer

#다른사람 답
def solution(s):
    #굳이 리스트로 안만들고 sorted를 쓰면 리스트형태로 됨.
    return ''.join(sorted(s, reverse=True))

#가운데 글자 가져오기
#https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    if len(s)%2 == 0:
        answer = s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        answer = s[int(len(s)/2)]
    return answer

solution("abcde")
solution("qwer")

#이전 답
import math
def solution(s):
    answer = ''
    if len(s)%2 == 1:
        i = math.floor(len(s)/2)
        answer += s[i]
    else:
        j = int(len(s)/2-1)
        answer += s[j:j+2]
    return answer