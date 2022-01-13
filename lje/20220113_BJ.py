#백준
#다리 놓기
#https://www.acmicpc.net/problem/1010
def factorial(x):
    n = 1
    for i in range(1, x+1):
        n = n*i
    return n

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    answer = factorial(m) // (factorial(n) * factorial(m - n))
    print(answer)



#공바꾸기
#https://www.acmicpc.net/problem/10813

n,m = map(int, input().split())
num_list = []
for  i in range(1,n+1):
    num_list.append(str(i))

for i in range(m):
    f, s = map(int, input().split())
    num_list[s-1], num_list[f-1] = num_list[f-1], num_list[s-1]

print(' '.join(num_list))




