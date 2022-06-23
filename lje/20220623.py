#프로그래머스_SQL
#역순 정렬하기
#https://programmers.co.kr/learn/courses/30/lessons/59035
from math import floor


SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;

#여러 기준으로 정렬하기
#https://programmers.co.kr/learn/courses/30/lessons/59404
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC;

#프로그래머스
#[1차]뉴스 클러스터링
#https://programmers.co.kr/learn/courses/30/lessons/17677
import math
def word_split(x):
    x = x.lower()
    word_array = []
    for i in range(len(x)-1):
        if x[i:i+2].isalpha():
            word_array.append(x[i:i+2])
    return word_array
def solution(str1, str2):
    s1 = word_split(str1)
    s2 = word_split(str2)
    inter = []
    #remove를 해야하므로 copy하여 이용
    s1c = s1.copy()
    s2c = s2.copy()
    for i in s1:
        if i in s2c:
            inter.append(i)
            s1c.remove(i)
            s2c.remove(i)
    union = inter + s1c + s2c
    #교집합과 합집합이 0일 경우 곱할 수 인 65536 반환
    if len(inter) == 0 and len(union) == 0:
        return 65536
    return math.floor((len(inter)/len(union))*65536)

#참고
import math
def solution(str1, str2):
    s1 = make_2_word(str1)
    s2 = make_2_word(str2)
    print(s1,s2)
    if s1 == [] and s2 == []:
        return 65536

    s1_copy = s1.copy()
    s2_copy = s2.copy()

    # 교집합
    inter = []
    for i in s1:
        if i in s2_copy:
            inter.append(i)
            s1_copy.remove(i)
            s2_copy.remove(i)
    print(inter)


    # 합집합
    union = inter + s1_copy + s2_copy
    print(union)


    answer = math.floor((len(inter) / len(union)) * 65536)
    return answer


def make_2_word(s):
    s = s.upper()
    a = []
    for i in range(len(s) - 1):
        if s[i:i + 2].isalpha():
            a.append(s[i:i + 2])
    return a
solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")
print(0/5)