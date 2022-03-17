#호텔 방번호
import sys
while True:
    answer=0
    try:
        n, m= map(int, sys.stdin.readline().split())
    except:
        break
    rooms= [str(i) for i in range(n, m+1)]
    for room in rooms:
        sroom=''.join(set(list(room)))

        if len(sroom)!=  len(room):
            answer+=1
    print(answer)
        