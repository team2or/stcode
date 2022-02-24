#해커링크
#Revising the Select Query I(선택 쿼리 수정 I)
#https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
SELECT * FROM CITY WHERE CountryCode = 'USA' AND POPULATION >= 100000;

#Weather Observation Station 4(기상관측소4)
#https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true
SELECT count(CITY) - count(DISTINCT CITY) FROM STATION;

#프로그래머스
#해시
#전화번호 목록
#https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i-1] in phone_book[i] and phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
                return False
    return True

solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])


#다른답안(효율성이 더 좋음)
#zip으로 앞,뒤의 번호를 묶어서 추출후 startswith함수로 시작문자가 같은지 체크
#https://dpdpwl.tistory.com/119
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
