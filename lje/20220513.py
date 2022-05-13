#해커랭크
#복습
#Average Population
#https://www.hackerrank.com/challenges/average-population/problem?isFullScreen=true
from cgitb import text


SELECT floor(avg(POPULATION)) FROM CITY;

#프로그래머스
#행렬테두리 회전하기
#https://programmers.co.kr/learn/courses/30/lessons/77485
#답안
#https://velog.io/@evencoding/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.2-%ED%96%89%EB%A0%AC-%ED%85%8C%EB%91%90%EB%A6%AC-%ED%9A%8C%EC%A0%84%ED%95%98%EA%B8%B0
rows = 6
columns = 6
queries = [[2,2,5,4]]
array = [[0] * columns for _ in range(rows)]
num = 1
for i in range(rows):
    for j in range(columns):
        array[i][j] = num
        num += 1

answer = []
for x1, y1, x2, y2 in queries:
    temp = array[x1-1][y1-1]
    mi = temp
    for k in range(x1-1,x2-1): #왼쪽 세로
        test = array[k+1][y1-1]
        array[k][y1-1] = test
        mi = min(mi, test)
    for k in range(y1-1,y2-1): #하단 가로
        test = array[x2-1][k+1]
        array[x2-1][k] = test
        mi = min(mi, test)
    for k in range(x2-1,x1-1,-1): #오른쪽 세로(시계방향이므로 위에서 아래로)
        test = array[k-1][y2-1]
        array[k][y2-1] = test
        mi = min(mi, test)
    for k in range(y2-1,y1-1,-1): #상단 가로
        test = array[x1-1][k-1]
        array[x1-1][k] = test
        mi = min(mi, test)
    array[x1-1][y1] = temp
    answer.append(mi)
print(array)