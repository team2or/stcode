# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QKsLaAy0DFAUq&categoryId=AV5QKsLaAy0DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# SW Expert Academy 2047.

while True:
    headline = input("헤드라인을 입력해주세요 : ")
    # 내용이 없는 경우
    if bool(headline) == False:
        pass
    else:
        print(headline.upper())
        break
