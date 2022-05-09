#해커랭크
#복습
#Placements
#https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
SELECT A.Name FROM (SELECT S.ID, S.Name, P.Salary FROM Students S LEFT JOIN Packages P ON S.ID=P.ID) A LEFT JOIN (SELECT F.ID, F.Friend_ID, P.Salary FROM Friends F LEFT JOIN Packages P ON F.Friend_ID=P.ID) B ON A.ID=B.ID WHERE A.Salary < B.Salary ORDER BY B.Salary;

#프로그래머스
#삼각달팽이
#https://programmers.co.kr/learn/courses/30/lessons/68645
#답안:https://developnote.tistory.com/26
n=4
def solution(n):
    result = []
    x, y = -1, 0
    num = 1
    for i in range(1,n+1):
        result.append([0]*i)
        
    for i in range(n): #방향
        for j in range(i,n): #좌표구하기 
            if i%3==0: #아래로
                x += 1
            elif i%3==1: #오른쪽
                y+=1
            else: #위로
                x -= 1
                y -= 1
            result[x][y] = num
            num+=1
    return sum(result,[])