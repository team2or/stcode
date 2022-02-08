# 프로그래머스_SQL
# 동물의 아이디와 이름
# https://programmers.co.kr/learn/courses/30/lessons/59403
SELECT ANIMAL_ID, NAEM FROM ANIMAL_INS

# 아픈 동물 찾기
# https://programmers.co.kr/learn/courses/30/lessons/59036
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = 'Sick'

# 어린 동물 찾기
# https://programmers.co.kr/learn/courses/30/lessons/59037
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE NOT INTAKE_CONDITION = 'Aged'

# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899
# 1.3의 배수마다 자리수가 바뀜
# 2.3으로 나눈 나머지가 0이면 맨끝자리 4로 1이면 1로, 2이면 2로 끝남
# n이 0미만일 때까지 반복하여 3으로 나눈 후 더함.
# 다른 답안1
# https://latte-is-horse.tistory.com/127


def solution(n):
    answer = ''
    while n > 0:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += '4'
            n = n//3 - 1
    return answer[::-1]


solution(1)
solution(20)

# 다른 답안2
# https://nyeongnyeong.tistory.com/65


def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0:
            answer = '4' + answer
            n = n//3-1
        else:
            answer = str(n % 3) + answer
            n = n//3
    return answer


solution(1)
solution(20)
