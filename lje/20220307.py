#해커링크
#Employee Salaries
#https://www.hackerrank.com/challenges/salary-of-employees/problem?isFullScreen=true
SELECT name FROM Employee WHERE months < 10  AND salary > 2000 ORDER BY employee_id;

#Draw The Triangle 1
#https://www.hackerrank.com/challenges/draw-the-triangle-1/problem?isFullScreen=true
#SET으로 변수 설정
#REPEAT()함수로 문자('*') @NUMBER만큼 반복해서 출력
#information_schema.talbes: DB의 메타정보(테이블,칼럼,인덱스 등의 스키마정보)를 모아둔 DB
#P(20)까지 출력하라고 했으므로, LIMIT 20으로 설정
SET @NUMBER = 21;
SELECT REPEAT('*', @NUMBER := @NUMBER -1) FROM information_schema.tables LIMIT 20;

#[참고]
#https://velog.io/@nightnova96/SQLHackerRank-Draw-The-Triangle-12
#information_schema란?
#https://rk1993.tistory.com/entry/MySQLinformationschema%EB%9E%80-informationschema-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0

#프로그래머스
#깊이/너비 우선탐색(DFS/BFS)
#타겟넘버

def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    print(queue)
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        print(temp, idx)
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

solution([1,1,1,1,1], 3)
