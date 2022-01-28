#백준
#회의실 배정
#https://www.acmicpc.net/problem/1931
m = int(input())
t = []
count = 0
time = ()
for i in range(m):
    tt = tuple(map(int, input().split()))
    t.append(tt)
for i in sorted(t, key= lambda x:(x[1], x[0])):
    if time == ():
        time = i
        count += 1
    else:
        if time[1] <= i[0]:
            time = i
            count += 1
print(count)
#[참고]
#https://suri78.tistory.com/26
#1. 끝나는 시간의 오름차순 2. 시작하는 시간의 오름차순

#로프
#https://www.acmicpc.net/problem/2217
c = int(input())
rope = []
for i in range(c):
    r = int(input())
    rope.append(r)
rope.sort(reverse=True)
for i in range(c):
    rope[i] = rope[i] * (i+1)
print(max(rope))
