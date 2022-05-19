#프로그래머스_SQL
#복습
#이름에 el이 들어가는 동물 찾기
#https://programmers.co.kr/learn/courses/30/lessons/59047
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE NAME LIKE "%el%" AND ANIMAL_TYPE = "Dog" ORDER BY NAME; 

#점프와 순간이동
#https://programmers.co.kr/learn/courses/30/lessons/12980
#답안
#https://hkim-data.tistory.com/75
#n을 0으로 만드는 것이라 생각하고 %2가 0이 되면 순간이동
#%2가 1이면 점프로 건전지사용
n = 5000
ans = 0
while n > 0:
    if n%2 == 1:
        n -= 1
        ans += 1
    else:
        n //= 2
print(ans)
print(5//2)