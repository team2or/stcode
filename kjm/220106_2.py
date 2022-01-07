# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
# SW Expert Academy 1986.

T = int(input())
for i in range(1, T+1):
    N = int(input())
    total = 0
    for j in range(1, N+1):    
        # 홀수인 경우
        if j%2 == 1:
            total += j
        # 짝수인 경우
        else:
            total -= j

    print(f"#{i} {total}")