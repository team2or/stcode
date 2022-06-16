#해커랭크
#복습
#Revising Aggregations - Averages
#https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true
SELECT avg(POPULATION) FROM CITY WHERE DISTRICT = "California";

#Population Density Difference
#https://www.hackerrank.com/challenges/population-density-difference/problem?isFullScreen=true
SELECT max(POPULATION) - min(POPULATION) FROM CITY;


#프로그래머스
#해시
#위장
#https://programmers.co.kr/learn/courses/30/lessons/42578
#이전답안
def solution(clothes):
    answer = 1
    wear = {}
    for c in clothes:
        if c[1] in wear.keys():
            wear[c[1]].append(c[0])
        else:
            wear[c[1]] = [c[0]]
    for cloth in wear.keys():
        answer = answer * (len(wear[cloth]) + 1)
    return answer -1

#이번답안
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes_dic = {}
for c in clothes:
    if c[1] in clothes_dic.keys():
        clothes_dic[c[1]].append(c[0])
    else:
        clothes_dic[c[1]] = [c[0]]
answer = 1
for i in clothes_dic.keys():
    answer = answer * (len(clothes_dic[i])+1)
print(answer -1)













