# 프로그래머스_SQL
#고양이와 개는 몇 마리 있을까
#https://programmers.co.kr/learn/courses/30/lessons/59040
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) as count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE;

#동명 동물 수 찾기
#https://programmers.co.kr/learn/courses/30/lessons/59041
SELECT NAME, COUNT(NAME) "COUNT" FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING COUNT(NAME) > 1 ORDER BY NAME;

#짝지어 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12973

#stack이용
#https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%A7%9D%EC%A7%80%EC%96%B4-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0
#정답
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if len(stack) != 0:
        return 0
    else:
        return 1
solution("baabaa")
solution("cdcd")

#내답-중도포기
def solution(s):
    answer = -1
    s = list(s)
    while len(s) > 1:
        for i in range(1,len(s)+1):
            if s[i-1] == s[i]:
                del s[i-1]
                del s[i]
                break
    print(s)
    return answer
solution("baabaa")
