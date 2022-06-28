#해커랭크
#New Companies
#https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
#참고: https://ehdals9412.tistory.com/m/40
SELECT C.company_code, C.founder, count(DISTINCT LM.lead_manager_code), count(DISTINCT SM.senior_manager_code), count(DISTINCT M.manager_code), count(DISTINCT E.employee_code) FROM Company C
JOIN Lead_Manager LM ON C.company_code=LM.company_code
JOIN Senior_Manager SM ON C.company_code=SM.company_code
JOIN Manager M ON C.company_code=M.company_code
JOIN Employee E ON C.company_code=E.company_code
GROUP BY C.company_code, C.founder
ORDER BY C.company_code;


#프로그래머스
#소수구하기
#https://programmers.co.kr/learn/courses/30/lessons/12921
#참고: https://seongonion.tistory.com/43
#시간초과
n=5
def prime_num(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

answer = 0
for k in range(2,n+1):
    if prime_num(k) == True:
        answer += 1
print(answer)

#에라토스테네스의 체
def prime_num(n):
    arr = [True] * (n+1)
    arr[0], arr[1] = False, False

    for i in range(2,n+1):
        if arr[i] == True:
            j = 2
            while (i*j) <= n:
                arr[i*j] = False
                j += 1
    return arr

arr = prime_num(n)
answer = 0
for i in range(len(arr)):
    if arr[i] == True:
        answer += 1