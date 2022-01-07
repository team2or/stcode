#SW Expert Academy

#문제1
#1대1 가위바위보 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=2

n = list(map(int, input().split()))

if n[0] < n[1]:
    print('B')
else:
    print('A')

#문제2
#시각 덧셈 D2
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PttaaAZIDFAUq&categoryId=AV5PttaaAZIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=2

t = int(input())
for i in range(1, t+1):
    time = list(map(int,input().split()))
    h = time[0] + time[2]
    m = time[1] + time[3]
    answer = ""
    if h < 13 and m < 60:
        answer += f'{h} {m}'
    elif h < 13 and m < 120:
        answer += f'{h+1} {m-60}'
    elif h > 12 and m < 60:
        answer += f'{h-12} {m}'
    else:
        answer += f'{(h-12)+1} {m-60}'
    print(f'#{i} {answer}')