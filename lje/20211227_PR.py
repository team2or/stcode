#프로그래머스
#시저암호
#https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            num = ord(i) + n
            if num > 64 and num < 91:
                answer += chr(num)
            elif num > 90:
                answer += chr(num - 26)
        elif i.islower():
            num = ord(i) + n
            if num > 96 and num < 123:
                answer += chr(num)
            elif num > 122:
                answer += chr(num - 26)
        else:
            answer += i
    return answer

solution("ASYZ c      z",4)