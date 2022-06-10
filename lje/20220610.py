#해커랭크
#복습
#SQL Project Planning
#https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true
#참고: https://techblog-history-younghunjo1.tistory.com/170
'''1.시작날짜가 종료날짜에 없어야 하고 종료날짜가 시작날짜에 없어야 함
2.시작날짜가 종료날짜보다 빨라야함
3.시작날짜로 그룹핑 시작-종료일 차이가 적은 순부터 정렬
** 종료날짜의 최솟값을 출력해야 함'''
SELECT Start_Date, min(End_Date) FROM (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) tab1, (SELECT End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) tab2 WHERE Start_Date < End_Date GROUP BY Start_Date ORDER BY DATEDIFF(MIN(End_Date), Start_Date), Start_Date;

#프로그래머스
#[3차]압축
#https://programmers.co.kr/learn/courses/30/lessons/17684
msg = "KAKAO"
dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
answer = []
s = msg[0]
i = 0
while i != len(msg):
    if s in dic:
        if i != len(msg)-1:
            i += 1
        else:
            answer.append(dic.index(s)+1)
            break
        s += msg[i]
    else:
        dic.append(s)
        answer.append(dic.index(s[:-1])+1)
        s = msg[i]

#다른답안
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer

