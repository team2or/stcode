#SW Expert Academy
#1859. 백만 장자 프로젝트 D2
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))[::-1] #뒤에서부터 시작
    best_price = n_list[0]
    revenue = 0
    for i in range(n):
        if best_price >= n_list[i]:
            revenue += best_price-n_list[i]
        else:
            best_price = n_list[i]
    print(f'#{test_case} {revenue}')