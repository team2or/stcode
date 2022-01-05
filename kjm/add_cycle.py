n = num = int(input())
cnt = 0
while True:
    add = (num//10) + (num%10)
    result = ((num%10)*10) + (add%10)
    cnt += 1
    if n == result:
        print(cnt)
        break
    else:
        num = result