#문제1
from torch import Graph


score = {"A":5, "B":4, "C":3, "D":2, "E":1, "F":0}
scores = ["AAFAFA", "FEECAA", "FABBCB", "CBEDEE", "CCCCCC"]

count = 0
for s in scores:
    s = sorted(list(map(str, ''.join(s))))
    if s.count("F") < 2:
        if s.count("A") >= 2:
            count += 1
        else:
            print(s)
            total = 0
            s = s[1:-1]
            print(s)
            for i in s:
                total += score[i]
            if total/len(s) >= 3:
                count += 1
print(count)

#답안: 통과
def solution(scores):
    score = {"A":5, "B":4, "C":3, "D":2, "E":1, "F":0}
    count = 0
    for s in scores:
        s = sorted(list(map(str, ''.join(s))))
        if s.count("F") < 2:
            if s.count("A") >= 2:
                count += 1
            else:
                total = 0
                s = s[1:-1]
                for i in s:
                    total += score[i]
                if total/len(s) >= 3:
                    count += 1
    return count


#문제2
def solution(needs, r):
    answer = 0
    return answer

needs = [ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ]
r = 2
factory = [[] for _ in range(len(needs))]
print(factory)
for i in range(len(needs)):
    for j in range(len(needs[i])):
        if needs[i][j] == 1:
            factory[i].append(j)
robot = [i for i in range(len(needs[i]))]
count = 0
for i in range(16):
    ro = robot[i:i+2]
    for f in factory:
        
f = [[], [], [], [], [], []]
for i in range(len(f)):
    for j in range(3):
        f[i].append(i)
print(f)


#문제3
import re

record = ["id=1 sit k=1","id=2 sit k=3","id=3 sit k=2","id=2 leave","id=4 sit k=4","id=5 sit k=2"]
record = ["id=1 sit k=6","id=1 leave","id=2 sit k=1","id=3 sit k=5","id=4 sit k=2"]
sits = []
answer = []
for r in record:
    print(r)
    r = r.split()
    if len(r) == 3:
        id = int(re.sub(r'[^0-9]', '', r[0]))
        k = int(re.sub(r'[^0-9]', '', r[2]))
        space = (k*2)+1
        if len(sits) == 0:
            sits += list(map (str, '0'*k + f'{id}' + '0'*k))
            answer.append([id, sits.index(str(id))])
        else:
            for i in range(len(sits)):
                if sum([int(i) for i in sits[i:space+i]]) == 0:
                    sits[i:space] = list(map (str, '0'*k + f'{id}' + '0'*k))
                    answer.append([id, sits.index(str(id))])
                    break
    else:
        id = re.sub(r'[^0-9]', '', r[0])
        sits[sits.index(id)] = 0
        a = [i[0] for i in answer]
        answer.pop(a.index(int(id)))
    print(sits)
print(sorted(answer, key=lambda x:x[0]))
print(sits)
a = ['0','1','2','3']
a[1:3] = ['0','5']
print(a[5:])
