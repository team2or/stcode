#해커랭크
#The Report
#https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true
SELECT CASE WHEN G.Grade < 8 THEN NULL ELSE S.Name END,
G.Grade, S.Marks FROM Students AS S
JOIN Grades AS G ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
ORDER BY G.Grade DESC, S.Name, S.Marks;
#[참고]
#https://velog.io/@develop_wan/MSSQL-%ED%95%B4%EC%BB%A4%EB%9E%AD%ED%81%ACHackerRank-The-Report
#비등가조인
#https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=pjok1122&logNo=221542110221

#Ollivander's Inventory
#https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
#영어라 문제가 잘 이해도지 않아 해설을 찾아봄
#조건
#1. is_evil = 0인 지팡이
#2. age, power값이 각각 같은 지팡이들 중 coins_needed가 최소인 값
#3. 정렬은 power, age 순으로 내림차순 정렬
#4. 출력은 id, age, coins_needed, power 순으로 출력해야 함
#
SELECT W.id, WP.age, W.coins_needed, W.power FROM Wands W
JOIN Wands_Property WP ON W.code = WP.code
WHERE WP.is_evil = 0
AND W.coins_needed = (SELECT min(W1.coins_needed)FROM Wands W1 INNER JOIN Wands_Property P1 ON W1.code = P1.code WHERE P1.is_evil = 0 AND W1.power = W.power AND P1.age=WP.age)
ORDER BY W.power DESC, WP.age DESC;

#답안1
#https://techblog-history-younghunjo1.tistory.com/165
#답안2-해설이 잘되어 있음
#https://velog.io/@yeahxne/SQLHackerRankOllivanders-Inventory

#프로그래머스
#해시
#완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576
#효율성 테스트에서 모두 시간초과 뜸
def solution(participant, completion):
    while completion:
        com = completion.pop()
        if com in participant:
            participant.remove(com)
    return participant[0]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])

#[참고]
#https://velog.io/@huga/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%95%B4%EC%8B%9C-%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80-%EB%AA%BB%ED%95%9C-%EC%84%A0%EC%88%98
#딕셔너리로 풀기
def solution(participant, completion):
    person = {}
    for part in participant:
        if part in person:
            person[part] += 1
        else:
            person[part] = 1
    for com in completion:
        if person[com] == 1:
            del person[com]
        else:
            person[com] -= 1
    
    return list(person.keys())[0]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])

#해시알고리즘으로 풀기
def solution(participant, completion):
    person = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        person += hash(part)
    print(person)
    print(dic)
    for com in completion:
        person -= hash(com)
    answer = dic[person]
    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])

#hash()함수에 문자를 넣으면 숫자로 변환
#동일한 문자면 동일한 숫자가 나오므로 participant에 모든 참가자의 해시를 더하고
#completion 완주자의 해시를 빼면 완주하지 못한 사람의 해시값만 남게 됨
#그 해시값을 해시값을 키로 값을 참가자 이름으로 정리한 사전에 키값으로 찾으면
#완주하지 못한 사람의 이름을 구할 수 있음