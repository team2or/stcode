#도서관
n,m = map(int, input().split())
books=list(map(int, input().split()))
if len(books)<1:
    print(0)
else:
    books.sort()

    left = [abs(i) for i in books if i < 0]
    right= [i for i in books if i > 0]
    left.sort()

    answer=0
    max_=0
    if len(left)> 0:
        max_=max(left)
        if len(right)>0:
            if max(left)< max(right):
                max_=max(right)

    if max_ in left :
        if max_ in right:
            if len(left)> len(right):
                for _ in range(m):
                    if len(left)>0:
                        left.remove(left[-1])
            else: 
                for _ in range(right)>0:
                    right.remove(right[-1])
        else:
            for _ in range(m):
                if len(left)>0:
                    left.remove(left[-1])
    else:
        for _ in range(m):
            if len(right)>0:
                right.remove(right[-1])

    right.reverse()
    left.reverse()
    
    answer+=sum([left[j] for j in range(0, len(left), m)])*2
    answer+=sum([right[j] for j in range(0, len(right), m)])*2
    answer+=max_
    print(answer)

right[1]


left = []
right = []
for item in book:
    if item < 0:
        left.append(item)
    elif item > 0:
        right.append(item)
left=[-5,-3,-2]
right=[2,1]
distance = []
left.sort()
for i in range(len(left)//m):
    distance.append(abs(left[m*i]))
if len(left) % m > 0:
    distance.append(abs(left[(len(left)//m)*m]))
    
right.sort(reverse = True)
for i in range(len(right)//m):
    distance.append(right[m*i]) 
if len(right) % m > 0:
    distance.append(right[(len(right)//m)*m])    
distance
distance.sort()
result = distance.pop()
result += 2*sum(distance)
print(result)    


n,m = map(int, input().split())
books=list(map(int, input().split()))
left = [i for i in books if i < 0]
right= [i for i in books if i > 0]
left.sort()
right.sort(reverse=True)

max_left=0
max_right=0

if len(left)>0:
    max_left=min(left)
if lent(right)>0:
    max_right=max(right)


if abs(max_left) >= max_right:
    max_=max_left
    for _ in range(m):
        left.remove(left[0])
else:
    max_=max_right
    for _ in range(m):
        if len(right)>0:
            right.remove(right[0])
answer=0
for i in range(0, len(left),m):
    answer+=left[i]*2
for j in range(0, len(right), m):
    answer+=right[j]*2
answer+=abs(max_)
print(answer)
