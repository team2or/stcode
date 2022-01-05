#SW Expert Academy

#문제1
#2027. 대각선 출력하기 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&contestProbId=AV5QFuZ6As0DFAUq&categoryId=AV5QFuZ6As0DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=2

answer = ''
for i in range(5):
    list = ['+']*5
    list[i] = ('#')
    answer += ''.join(list) + '\n'
print(answer.rstrip())

#문제2
#패턴 마디의 길이 D2
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

t = int(input())
for i in range(1,t+1):
    n = input()
    for j in range(1,10):
        if n[:j] == n[j:j*2]:
            print(f'#{i} {j}')
            break