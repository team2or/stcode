#해커랭크
#복습
#Weather Observation Station 5
#https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
SELECT CITY, length(CITY) FROM STATION ORDER BY length(CITY), CITY LIMIT 1;
SELECT CITY, length(CITY) FROM STATION ORDER BY length(CITY) DESC, CITY LIMIT 1;

#프로그래머스
#멀쩡한 사각형
#https://programmers.co.kr/learn/courses/30/lessons/62048
#답안
#https://eunhee-programming.tistory.com/135
def solution(s):
    result=[]
    if len(s)==1:
        return 1
    #쪼갤 수 있는 최대 길이가 문자열 s의 반이므로 len(s)//2    
    for i in range(1, (len(s)//2)+1):
        b = ''
        cnt = 1
        tmp=s[:i]

        #첫글자부터 끊어서 반복되는 횟수 카운트
        for j in range(i, len(s), i):
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b += str(cnt)+tmp
                else:
                    b += tmp
                tmp=s[j:j+i]
                cnt = 1
        if cnt!=1:
            b += str(cnt) + tmp
        else:
            b += tmp
        
        #각 슬라이싱의 결과값 저장
        result.append(len(b))
    return min(result)

solution("xababcdcdababcdcd")