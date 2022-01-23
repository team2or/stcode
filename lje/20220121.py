#프로그래머스
#튜플
#https://programmers.co.kr/learn/courses/30/lessons/64065
import re
def solution(s):
    answer = []
    num_list = []
    #{}제거
    for i in s.split('},'):
        num_list.append(re.sub('[[\{\]\}]', '',i))
    #문자 길이로 정렬
    num_list.sort(key=lambda x: len(x))
    #차례로 answer에 추가
    for i in num_list:
        if len(i) == 1:
            answer.append(int(i))
        else:
            for num in i.split(','):
                if int(num) not in answer:
                    answer.append(int(num))
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")

#SW Expert Academy
#13229. 일요일 D3
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AX0SaDW6L2oDFASs&categoryId=AX0SaDW6L2oDFASs&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

t = int(input())
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for i in range(1,t+1):
    day = input()
    num = 7 - days.index(day)
    print(f'#{i} {num}')
