#문제1
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
def solution(survey, choices):
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    result = {}
    for sur, cho in zip(survey, choices):
        f, s = map(str, sur)
        if cho >= 4:
            if s not in result.keys():
                result[s] = score[cho]
            else:
                result[s] += score[cho]
        else:
            if f not in result.keys():
                result[f] = score[cho]
            else:
                result[f] += score[cho]
    types = [["R","T"], ["C","F"],["J","M"],["A","N"]]
    answer = ''
    for t1, t2 in types:
        if t1 in result.keys() and t2 in result.keys():
            if result[t1] >= result[t2]:
                answer += t1
            else:
                answer += t2
        elif t1 in result.keys() and t2 not in result.keys():
            answer += t1
        elif t1 not in result.keys() and t2 in result.keys():
            answer += t2
        else:
            answer += t1
    return answer

#문제2
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
target = int((sum(queue1)+sum(queue2))/2)
while sum(queue1) == target:
    break

#문제3
alp = 10
cop = 10
hour = 0
problems = [[10,15,2,1,2],[20,20,3,3,4]]
while problems:
    p = problems.pop(0)
    if len(problems):
        if alp >= p[0] and cop >= p[1]:
            alp += p[2]
            cop += p[3]
            hour += p[2]
        elif alp >= p[0] and cop < p[1]:
            while cop >= p[1]:
                cop += 1
                hour += 1
        
    else:
        print(hour)
#문제4
n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
roads = [[] for _ in range(n+1)]
for r in paths:
    roads[r[0]].append([r[2], r[1]])
    roads[r[1]].append([r[2], r[0]])