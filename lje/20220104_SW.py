#SW Expert Academy

#문제1
#2043. 서랍의 비밀번호 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QJ_8KAx8DFAUq&categoryId=AV5QJ_8KAx8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2&&&&&&&&&&

P, K = map(int, input().split())

Kplus = K
num = 1
stop = True
while stop:
    if P != Kplus:
        num += 1
        Kplus += 1
    elif P == Kplus:
        stop = False
        print(num)


#문제2
#2063. 중간값 찾기 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

n = int(input())
v = sorted(list(map(int, input().split())))
half = int(n/2)
print(v[half])