#프로그래머스_SQL
#아픈동물찾기
#https://programmers.co.kr/learn/courses/30/lessons/59036
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = "Sick" ORDER BY ANIMAL_ID;

#상위 n개 레코드
#https://programmers.co.kr/learn/courses/30/lessons/59405
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;

#프로그래머스
#행렬의 곱셈
#https://programmers.co.kr/learn/courses/30/lessons/12949
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = 	[[3, 3], [3, 3]]
answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
for i in range(len(arr1)):
    for j in range(len(arr2[0])):
        for k in range(len(arr1[0])):
            answer[i][j] += (arr1[i][k] * arr2[k][j])
print(answer)

#다른답안
#https://hodunamu.com/python-%ED%96%89%EB%A0%AC%EC%9D%98-%EA%B3%B1%EC%85%88/
#https://www.delftstack.com/ko/howto/numpy/python-numpy-matrix-vector-multiplication/
import numpy as np

def solution(arr1, arr2):
    # answer = np.dot(arr1, arr2).tolist()
    answer = np.matmul(arr1,arr2).tolist()
    return answer
solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])