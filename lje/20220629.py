#SQLZOO
#SELECT_basics
#1
SELECT population FROM world WHERE name = 'Germany';
#2
SELECT name, population FROM world WHERE name IN ('Sweden', 'Norway', 'Denmark');
#3
SELECT name, area FROM world WHERE area BETWEEN 200000 AND 250000;

#프로그래머스
#두개뽑아서 더하기
#https://programmers.co.kr/learn/courses/30/lessons/68644
from itertools import permutations
numbers = [2,1,3,4,1]
num = list(permutations(numbers, 2))
answer = []
for n in num:
    s = n[0]+n[1]
    if s not in answer:
        answer.append(s)
print(sorted(answer))

#다른답안
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))