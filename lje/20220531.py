#해커랭크
#복습
#Higher Than 75 Marks
#https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true
#이름 끝 3자리로 정렬하지만 동일한 끝 3자리일 경우 ID로 정렬
SELECT Name FROM STUDENTS WHERE Marks > 75 ORDER BY right(Name,3), ID;

#프로그래머스
#n^2 배열 자르기
#https://programmers.co.kr/learn/courses/30/lessons/87
#내 답안: 시간초과
from collections import deque
n = 4
left = 7
right = 14
array = [[0]*n for _ in range(n)]
dx, dy = [1,1,0],[1,0,1]
q = deque()
q.append([0,0])
num = 1
array[0][0] = num
while q:
    x, y = q.popleft()
    if x == y:
        num += 1
    for i in range(3):
        nx, ny = dx[i]+x, dy[i]+y
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if array[nx][ny] == 0:
                array[nx][ny] = num
                q.append([nx,ny])
array = sum(array,[])
print(array[left:right+1])

#제한사항의 범위가 크기 때문에 위처럼하면 엄청난 시간과 용량이 필요함
#left와 right에 해당되는 수만 구해야 함
#해답
#https://2hs-rti.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv2-n2-%EB%B0%B0%EC%97%B4-%EC%9E%90%EB%A5%B4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
#2차원 배열과 1차원 배열의 인덱스 값은 (i//n, i% n)과 같은 관계가 있음
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer