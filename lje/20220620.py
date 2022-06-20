#해커랭크
#복습
#Weather Observation Station 12
#https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true
#참고: https://www.codeworld19.com/weather-observation-station-12-sql-hacker-rank-solution/
#[]앞 뒤에 ^,$는 시작문자, 끝문자
#[]안 맨앞에 붙인 ^는 not의 의미
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^aeiouAEIOU]' AND CITY REGEXP '[^aeiouAEIOU]$';
