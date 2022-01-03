#백만 장자 프로젝트
import random
T=int(input()) #테이스케이스 개수
N=int(input())
case=[] #매매가 
answer=[]
for i in range(0,T):
    interests=0 #이익 
    for j in range(N):
        money=random.randint(1,10000)
        case.append(money)
    for k in range(len(case)):
        interests+=max(case)-case[i]
        case[i]=0
    answer.append(f"#{i+1} {interests}")

for i in answer:
    print(i, end='\n')
############################input값 T N 각날의 매매가 받기

T = int(input())
for t in range(1,T+1):
    num = int(input())
    arr = list(map(int,input().split()))
    last = arr[-1]
    cnt = 0
    for i in range(len(arr)-1,-1,-1): # 핵심! 뒤부터 보기
        if last > arr[i]:
            cnt += last-arr[i]
        else: # 같거나 작을 때 
            last = arr[i]
    print("#{} {}".format(t, cnt))

for test in range(1,int(input())+1):
    N = int(input())
    prices = list(map(int, input().split()))
    answer = 0
    max_price = 0 
    for j in range(N-1,-1,-1):
        if max_price > prices[j]:
            answer += max_price - prices[j]
        else:
            max_price = prices[j]

    print(f'#{test} {answer}')

########################################

list(map(int, input().split())) #숫자 입력값을 공백을 기준으로 나누어 리스트에 저장

T=int(input())
for i in range(1, T+1):
    n=int(input())
    price=list(map(int, input().split()))
    interests=0
    for j in range(len(price)):
        interests+=max(price)-price[j]
        print(max(price))
        price[j]=0
    print(f"#{i} {interests}")

#####################시간초과 오류 N이 커지면 최댓값을 구하는 과정에서 오류가 난다고 한다.

##뒤에서 부터 구하는 방법으로 

T=int(input())
for i in range(1, T+1):
    n=int(input())
    price=list(map(int, input().split()))
    interests=0
    max_price=price[-1]
    for j in price[::-1]:
        if max_price-j>0:
            interests+=max_price-j
        if (max_price-j)<=0:
            max_price=j
    print(f"#{i} {interests}")
