#해커랭크
#Weather Observation Station 19
#https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true
#Euclidean Distance: sart((a-b)**2 + (c-d)**2)
SELECT round(sqrt(pow(max(LAT_N) - min(LAT_N),2) + pow(max(LONG_W)-min(LONG_W),2)),4) FROM STATION;

#The PADS
#https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
#문자열 자르기:http://chongmoa.com/sql/9155
#문자열 합치기:https://extbrain.tistory.com/52
#모든 출력 concat으로 합쳐 하나로 출력
#이름과 직업의 첫글자 출력. 이름순으로 정렬
SELECT concat(Name, '(',left(Occupation, 1),')') FROM OCCUPATIONS ORDER BY Name;
#직업수 카운팅하여 출력. 직업은 소문자로 출력. 카운팅 수로 오름차순, 직업명 알파벳순으로 정렬
SELECT concat('There are a total of ', count(*),' ', lower(Occupation),'s.')
FROM OCCUPATIONS GROUP BY Occupation ORDER BY count(*), Occupation;

#백준
#해시, 자료구조, 이분탐색, 트리를 사용한 집합과 맵
#수찾기
#https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
a.sort() #리스트 정렬/함수안에서 정렬하면 계속 정렬하느라 시간초과 뜸
m = int(input())
m_list = list(map(int,input().split()))

def binary(target, a):
    start = 0
    end = len(a) -1
        
    while start <= end:
        mid = (start+end)//2
        if a[mid] == target:
            return print(1)
        elif a[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return print(0)

for m in m_list:
    binary(m, a)

#[참고]
#이분(이진)탐색
#https://wayhome25.github.io/cs/2017/04/15/cs-16/

#다른 답안
#https://alpyrithm.tistory.com/2
#이진탐색 재귀
def binary(a, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    if a[mid] == target:
        return True
    elif a[mid] > target:
        return binary(a, target, start, mid-1)
    else:
        return binary(a, target, mid+1, end)

import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
a.sort() #리스트 정렬/함수안에서 정렬하면 계속 정렬하느라 시간초과 뜸
m = int(input())
m_list = list(map(int,input().split()))

for m in m_list:
    if binary(a, m, 0, n-1):
        print(1)
    else:
        print(0)