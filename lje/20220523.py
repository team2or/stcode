#프로그래머스_SQL
#복습
#루시와 엘라 찾기
#https://programmers.co.kr/learn/courses/30/lessons/59046
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty");

#프로그래머스
#짝지어 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    s_list = list(s)
    stack = []
    for i in s_list:
        if len(stack) > 0:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0
solution("baabaa")
solution("cdcd")