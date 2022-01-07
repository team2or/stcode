# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&
# SW Expert Academy 2007.

T = int(input())
for i in range(1, T+1):
    text = input()
    for j in range(1, 11):
        if text[:j] == text[j:j+j]:
            break
    print(f"#{i} {j}")
