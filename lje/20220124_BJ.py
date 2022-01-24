#백준
#동전 0
#https://www.acmicpc.net/problem/11047
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
count = 0
for i in sorted(coins, reverse=True):
    count += k//i
    k = k%i
print(count)

#대회 or 인턴
#https://www.acmicpc.net/problem/2875

#예제와 다른 수 입력했을 때 잘 나오는 것 같은데
#왜 틀린지 모르겠음
n, m, k = map(int,input().split())
answer = 0
for i in range(0,k+1):
    nr = (n-i)//2
    mr = m-(k-i)-nr
    if mr >= 0 and answer < nr:
        answer = nr
print(answer)

#다른 정답1
n, m, k = map(int,input().split())
#for문을 돌면서 인턴쉽에 필요한 인원 제외
for i in range(k):
    #여학생//2 인원이 남학생 인원보다
    #많거나 같으면 여학생에서 제외
    if n//2 >= m:
        n -= 1
    #여학생//2 인원이 남학생 인원보다
    #적으로 남학생에서 제외
    else:
        m -= 1
#인턴쉽 참여인원 제외하고
#남은 학생 수에서 여학생//2와 남학생 중 최소값 반환
print(min(n//2,m))

#다른 정답2
n, m, k = map(int,input().split())
answer = 0
#2, 1 팀으로 빼고, 여,남학생 합이 3이상 k명 이상 일때,
while n >= 2 and m >= 1 and n+m >= k+3:
    n -= 2
    m -= 1
    answer += 1
print(answer)