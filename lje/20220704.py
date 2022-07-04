#SQLZOO
#SELECT from WORLD Tutorial
#https://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial
#1
SELECT name, continent, population FROM world;
#2
SELECT name FROM world WHERE population > 200000000;
#3
#1인당 GDP 구하기
SELECT name, (gdp/population) FROM world WHERE population > 200000000;
#4
SELECT name, (population/1000000) FROM world WHERE continent = 'South America';
#5
SELECT name, population FROM world WHERE name IN ('France', 'Germany', 'Italy');

#백준
#DP
#파일합치기
#https://www.acmicpc.net/problem/11066
#답안: https://roamingman.tistory.com/57
import math

def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    rst = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1, n):
        for i in range(j-1, -1, -1):
            small = math.inf
            for k in range(j-i):
                small = min(small, rst[i][i+k] + rst[i+k+1][j])
            rst[i][j] = small + sum(arr[i:j+1])
            print(rst)
    print(rst[0][n-1])

t = int(input())
for _ in range(t):
    solve()
