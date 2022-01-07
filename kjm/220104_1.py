# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QJ_8KAx8DFAUq&categoryId=AV5QJ_8KAx8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
# SW Expert Academy 2043.

P, K = map(int, input().split()) 
cnt = 0
for i in range(K, P+1):
    cnt += 1
    if i == P:
    	print(cnt)
