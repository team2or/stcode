# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc#none
# SW Expert Academy 1859.


# 1) 시간 초과
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    price_list = list(map(int,input().split()))
    total = 0
    
    for i in range(N):
        try:
            if price_list[i] < max(price_list[i:]):
                total += (max(price_list[i:]) - price_list[i])
        except ValueError:
            pass
            
    print(f"# {test_case} {total}")

# 2) 
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    price_list = list(map(int,input().split()))
    price_list = price_list[::-1]
    max_ = price_list[0]
    total = 0
    for i in range(1,len(price_list)):
        if max_ > price_list[i]:
            total += max_-price_list[i]
        else:
            max_ = price_list[i]
    print(f"#{test_case} {total}")