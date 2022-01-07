#SW Expert Academy

#문제1
#지그재그 숫자 D2
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&

t = int(input())
for i in range(1,t+1):
    n = int(input())
    answer = 0
    for j in range(1,n+1):
        if j%2 == 0:
            answer -= j
        else:
            answer += j
    print(f'#{i} {answer}')


#문제2
# 간단한 369게임 D2
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&

n = int(input())
for i in range(1,n+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        answer = ''
        for j in str(i):
            if j in ['3','6','9']:
                answer += '-'
        else:
            answer += ''
        print(answer, end=' ')
    else:
        print(i, end=' ')