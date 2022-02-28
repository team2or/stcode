#해커링크
#Weather Observation Station 6(기상관측소6)
#https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE SUBSTR(CITY, 1, 1) IN ('a', 'e', 'i', 'o', 'u');

#Weather Observation Station 7(기상관측소7)
#https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
SELECT DISTINCT CITY FROM STATION WHERE SUBSTR(CITY, -1, 1) IN ('a', 'e', 'i', 'o', 'u');

#[참고]
#SUBSTR()함수로 문자열 슬라이싱
#https://lcs1245.tistory.com/entry/SQL-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9E%90%EB%A5%B4%EA%B8%B0-SUBSTR-SUBSTRING-LEFT-RIGHT


#프로그래머스
#해시
#위장
#https://programmers.co.kr/learn/courses/30/lessons/42578
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

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])

#다른 답안
def solution(clothes):
    clothes_type = {}

    for t in clothes:
        if t not in clothes_type:
            #처음엔 안입는 경우와 하나 입을 경우 2가지이므로 2로 시작
            clothes_type[t[0]] = 2
        else:
            clothes_type[t[0]] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

#[참고]
#경우의 수
#https://namu.wiki/w/%EA%B2%BD%EC%9A%B0%EC%9D%98%20%EC%88%98
