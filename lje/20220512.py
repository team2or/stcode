#해커랭크
#복습
#Draw The Triangle 1
#https://www.hackerrank.com/challenges/draw-the-triangle-1/problem?isFullScreen=true
#set으로 변수 설정 후 값 지정
#REPEAT을 사용하여 number가 0일될 때까지 반복시킴
#information_schema.tables 테이블 사용
from turtle import st


set @number = 21;
SELECT REPEAT('* ', @number := @number-1) FROM information_schema.tables;

#프로그래머스
#스택/큐
#괄호회전하기
#https://programmers.co.kr/learn/courses/30/lessons/76502
#답안
#https://zoozoozoo.tistory.com/274
s = "[](){}"
s_list = list(s)
answer = 0
for _ in range(len(s)):
    stack = []
    for i in range(len(s_list)):
        if len(stack) > 0:
            if stack[-1] == "(" and s_list[i] == ")":
                stack.pop()
            elif stack[-1] == "[" and s_list[i] == "]":
                stack.pop()
            elif stack[-1] == "{" and s_list[i] == "}":
                stack.pop()
            else:
                stack.append(s_list[i])
        else:
            stack.append(s_list[i])
    if len(stack) == 0:
        answer += 1
    s_list.append(s_list.pop(0))
print(answer)
        