#SQLZOO
#SELECT names 1~10
#https://sqlzoo.net/wiki/SELECT_names
#1
SELECT name FROM world WHERE name LIKE 'Y%';
#2
SELECT name FROM world WHERE name LIKE '%y';
#3
SELECT name FROM world WHERE name LIKE '%x%';
#4
SELECT name FROM world WHERE name LIKE '%land';
#5
SELECT name FROM world WHERE name LIKE 'C%' AND name LIKE '%ia';
#6
SELECT name FROM world WHERE name LIKE '%oo%';
#7
#Find the countries that have three or more a in the name
SELECT name FROM world WHERE name LIKE '%a%a%a%';
#8
SELECT name FROM world WHERE name LIKE '_t%' ORDER BY name;
#9
SELECT name FROM world WHERE name LIKE '%o__o%';
#10
SELECT name FROM world WHERE name LIKE '____';

#프로그래머스
#3진법뒤집기
#https://programmers.co.kr/learn/courses/30/lessons/68935
#참고 - 진수변환
#https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95

#10진수 → n진수 메소드
def change_num(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    #역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    #해당문제는 앞뒤반전해야 되므로 뒤집지 않음
    return rev_base

ternary = change_num(45,3)
print(int(ternary,3))

