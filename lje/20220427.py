#프로그래머스
#복습
#입양시각구하기(2)
#https://programmers.co.kr/learn/courses/30/lessons/59413
from torch import combinations


WITH RECURSIVE h AS (SELECT 0 AS hour UNION ALL SELECT hour+1 FROM h WHERE hour <23)
SELECT hour, count(ANIMAL_ID) FROM h LEFT JOIN ANIMAL_OUTS ON hour = hour(DATETIME) GROUP BY hour;

#프로그래머스
#이진분법, 해시, 모든조합
#순위검색
#https://programmers.co.kr/learn/courses/30/lessons/72412
#답안:https://hongcoding.tistory.com/56
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    info_dict = {}
    for i in info:
        i = i.split()
        info_key = i[:-1] #점수 제외 값 key로 분류
        info_val = i[-1] #점수를 val로 분류

        for j in range(5): #key들로 만들 수 있는 모든 조합 생성
            for c in combinations(info_key, j):
                c = ''.join(c)
                if c in info_dict:
                    info_dict[c].append(int(info_val)) #해당 조합 key값에 점수 추가
                else:
                    info_dict[c] = [int(info_val)]

    #dict val의 값들을 오름차순으로 정리
    for k in info_dict:
        info_dict[k].sort()

    for q in query:
        q = q.split()
        q_key = q[:-1]
        q_val = q[-1]

        for _ in range(3):
            q_key.remove("and")
        while "-" in q_key:
            q_key.remove("-")
        q_key = ''.join(q_key)

        #해당 조합이 존재하는지 체크
        #없으면 0으로 결과 추가
        if q_key in info_dict:
            scores = info_dict[q_key]
            if scores:
                #점수가 주어졌을 때 해당 점수 이상을 받은 사람을 모두 구해야 하므로
                #왼쪽에서부터 해당 점수미만인 사람들 구함
                enter = bisect_left(scores, int(q_val))
                #구한 사람들을 모든 점수 수에서 빼면 해당 점수 이상받은 사람을 구할 수 있음
                answer.append(len(scores)-enter)
        else:
            answer.append(0)
    return answer

