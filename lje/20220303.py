#해커링크
#Weather Observation Station 10
#https://www.hackerrank.com/challenges/weather-observation-station-10/problem?isFullScreen=true
#[^] 이 코드 자체가 부정 ^이 들어갔다고 맨앞 표시 아님
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP "[^aeiou]$";

#Higher Than 75 Marks
#https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true
SELECT Name FROM STUDENTS WHERE Marks > 75 ORDER BY SUBSTR(Name, -3, 3), ID;

#[참고]
#ORDER BY 여러개: ','로 이어 씀
#https://mingggu.tistory.com/83
#문자열 슬라이싱
#시작위치를 -1, 길이를 3으로 하면 -1부터 차례로 3글자 출력인줄 알았는데
#시작위치 -3으로 해야 뒤에서 3번째부터 길이 3글자 출력으로 됨
#https://jhnyang.tistory.com/267

#프로그래머스
#정렬
#가장 큰 수

#실패
def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key=str)
    while len(numbers) > 0:
        num = str(numbers.pop())
        if num[-1] == '0' and len(numbers) > 0:
            numbers.insert(0, num)
        else:
            answer += num
    return str(int(answer))


#다른 답안(둘 다 테스트 시간은 엇비슷하다)
#https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html
def solution(numbers):
    numbers = list(map(str, numbers))
    num = sorted(numbers, key=lambda x:x*3, reverse=True)
    return str(int(''.join(num)))

#https://gurumee92.tistory.com/161
#원소 0~1000이하이므로 4자리로 문자열을 맞춰서 정렬
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:(x*4)[:4], reverse=True)
    return str(int(''.join(numbers)))