# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PttaaAZIDFAUq&categoryId=AV5PttaaAZIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=2
# SW Expert Academy 1976.

T = int(input())
for i in range(1, T+1):
    N = input().split(" ")
    t = 0
    m = 0
    for j in range(len(N)):
        if j%2 == 0:
            t += int(N[j])
        else:
            m += int(N[j])
    
    if t > 12:
        t -= 12
    
    if m >= 60:
        t += m//60
        m -= 60
    
    print(f"#{i} {t} {m}")