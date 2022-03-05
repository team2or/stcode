#기능개발
k,j= [93, 30, 55], [1, 30, 5]
from collections import deque

def solution(pro, speed):
    answer = []
    pro = deque(pro)
    speed = deque(speed)
    while pro:
        for i in range(len(pro)):
            pro[i]+=speed[i]
  
        cnt = 0
        while pro and pro[0]>=100:
            pro.popleft()
            speed.popleft()
            cnt+=1
            
        if cnt>=1:
            answer.append(cnt)
    return answer
    