#프로그래머스
#문제1
#https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    if len(s) == 4 or len(s) == 6: #문자열 길이 체크
        return s.isdigit()
    else:
        return False

#진수땜에 안되는 줄 알고 진수를 숫자로 변환하는 함수 만듦...
def solution(s):
    try:
        s = int(s,0)
    except:
        return False
    return str(s).isdecimal()

solution("0b0100111")

#문제2
#https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for i in range(2,1000001):
        if n%i == 1:
            return i
            break
        else:
            pass

solution(10)
solution(3)