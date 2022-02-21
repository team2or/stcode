#카드 정렬하기
n= int(input())
cards=[]
for _ in range(n):
    c=int(input())
    cards.append(c)
cards.sort()

answer=0
if len(cards)==1:
    print(0)
elif len(cards)==2:
    print(cards[0]+cards[1])
else:
    while len(cards)>1 :
        min1=cards.pop(0)
        min2=cards.pop(0)
        answer+=min1+min2
        cards.append(min1+min2)
        cards.sort()
        if len(cards)==2:
            answer+=cards[0]+cards[1]
            print(answer)


#카드 정렬하기
import heapq
n= int(input())
cards=[]
for _ in range(n):
    c=int(input())
    heapq.heappush(cards, c)
answer=0
if len(cards)==1:
    print(0)
elif len(cards)==2:
    print(cards[0]+cards[1])
else:
    while len(cards)>1 :
        min1= heapq.heappop(cards)
        min2= heapq.heappop(cards)
        answer+= min1+min2
        heapq.heappush(cards, min1+min2)
        if len(cards)==2:
            answer+=cards[0]+cards[1]
            print(answer)
