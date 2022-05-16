#해커랭크
#복습
#The Pads
#https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
#이름과 직업코드로 출력
#알파벳으로 정렬
SELECT concat(Name, 
CASE WHEN Occupation="Doctor" THEN "(D)"
WHEN Occupation="Professor" THEN "(P)"
WHEN Occupation="Singer" THEN "(S)"
WHEN Occupation="Actor" THEN "(A)" END) FROM OCCUPATIONS ORDER BY Name;
#각 직업별 수와 소문자로 직업 출력하는 문구 출력
#수가 적은 순, 같은 수라면 알파벳 순으로 정렬
SELECT concat("There are a total of ", count(Occupation), " ", lower(Occupation), "s.")
FROM OCCUPATIONS GROUP BY Occupation ORDER BY count(Occupation), Occupation;

#프로그래머스
#JadenCase 문자열 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12951

#이전답안
#제한조건 중 공백문자가 연속해서 나올 수 있다
#불만족으로 실패
def solution(s):
    s = list(map(str, s.split()))
    answer = []
    for i in s:
        answer.append(i.capitalize())
    return ' '.join(answer)

#최종답안
s = "3people unFollowed me"
s= "a a a a a a a a a a "
s= "a    a    a"
answer = ''
print(len(answer))
for i in range(len(s)):
    if s[i].isdigit() or s[i] == ' ':
        print(f"0: {s[i]}")
        answer += s[i]
    elif s[i].isalpha() and answer == '':
        print(f"1: {s[i]}")
        answer += s[i].upper()
    elif s[i].isalpha() and len(answer) > 0:
        if answer[-1] == ' ':
            print(f"2: {s[i]}")
            answer += s[i].upper()
        else:
            print(f"3: {s[i]}")
            answer += s[i].lower()
print(answer)


#다른답안
#1번답에서 split()을 " "(공백)으로 하고
#' '.join하면 되는 거였다...
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])

solution("a a   a")