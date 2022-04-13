#해커랭크
#복습
#Print Prime Numbers
#https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true
SET @prime = 1;
SET @divisor = 1;

SELECT GROUP_CONCAT(PRIME SEPARATOR '&') FROM
    (SELECT @prime := @prime + 1 AS PRIME FROM
    information_schema.tables t1,
    information_schema.tables t2
    LIMIT 1000) list_primes
WHERE NOT EXISTS(
    SELECT * FROM
        (SELECT @divisor := @divisor + 1 AS DIVISOR FROM
        information_schema.tables t1,
        information_schema.tables t2
        LIMIT 1000) list_divisors
    WHERE MOD(PRIME, DIVISOR) = 0 AND PRIME <> DIVISOR);

#프로그래머스
#여행경로
#https://programmers.co.kr/learn/courses/30/lessons/43164
def solution(tickets): 
    answer = []
    routes = {} # 티켓 정보를 저장하는 딕셔너리
    for start, end in tickets:
        if start not in routes:
            routes[start] = [end]
        else:
            routes[start] += [end]

    # 갈 수 있는 공항을 알파벳 역순으로 정렬
    for r in routes.keys():
        routes[r].sort(reverse = True)

    print(routes)
    st = ["ICN"]
    while st:
        print(st)
        print(answer)
        top = st[-1] # 스택 top을 start로 하는 티켓이 없는 경우
        if (top not in routes) or (not routes[top]):
            answer.append(st.pop()) # top을 스택에서 꺼내서 answer에 저장
        # 스택 top을 start로 하는 티켓이 있는 경우
        else:
            st.append(routes[top].pop())
    return answer[::-1]
solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
#출처: https://mjmjmj98.tistory.com/103