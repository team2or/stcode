# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AX0SaDW6L2oDFASs&categoryId=AX0SaDW6L2oDFASs&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# SW Expert Academy 13229.

T = int(input())
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
for test_case in range(1, T + 1):
    day = input().upper()
    if day == "SUN":
        d_day = 7
    else:
        d_day = 6 - days.index(day)
    
    print(f"#{test_case} {d_day}")