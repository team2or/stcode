# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&&&&&&&&&&&
# SW Expert Academy 1926.

N = int(input())
for i in range(1, N+1):
    cnt = 0
    i = str(i)
    for j in range(len(i)):
        if i[j] == "0":
            pass
        elif int(i[j])%3 == 0:
            cnt += 1
        else:
            pass
    if cnt == 0:
        print(i, end = " ")
    else:
        print("-"*cnt, end = " ")