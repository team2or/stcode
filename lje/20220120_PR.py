#프로그래머스
#신고 결과 받기
#https://programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    id_dic = {}
    result = {}
    answer = []
    for i in id_list:
        #신고누적횟수, 신고한 사람들 리스트
        id_dic[f'{i}'] = [0, '']
        #정답 딕셔너리
        result[f'{i}'] = 0
    #set()함수로 동일 신고 제거
    for i in set(report):
        #신고횟수 누적
        id_dic[f'{i.split(" ")[1]}'][0] += 1
        #신고한 사람 추가
        id_dic[f'{i.split(" ")[1]}'][1] += ' ' + i.split(" ")[0]

    for val in id_dic.values():
        if val[0] >= k:
            for i in val[1].split(' '):
                if i == '':
                    pass
                else:
                    #정지된 아이디를 신고한 사람에게 메일 보내기
                    result[i] += 1
    for i in result.values():
        answer.append(i)
    return answer
solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)

#다른사람 답
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    #아이디리스트 사전형으로 만듦
    reports = {x : 0 for x in id_list}

    #신고 누적
    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        #누적된 횟수가 k와 같을 때 해당 아이디 신고한 사람에게 메일보내기
        if reports[r.split()[1]] >= k:
            #리스트 인덱스로 동일한 위치에 숫자 더함
            answer[id_list.index(r.split()[0])] += 1

    return answer

#실패율
#https://programmers.co.kr/learn/courses/30/lessons/42889

#시간초과 뜸
def solution(N, stages):
    answer = []
    per = []
    for i in range(1,N+1):
        #계속 모든 길이 구하고 for문으로 참가자 구하는 건 시간 오래걸림
        num = len(stages)-sum([stages.count(j) for j in range(i)])
        #분모가 0일때 런타임 오류 뜸 -> 0일땐 0으로 처리
        if num > 0:
            #굳이 퍼센트로 변환 안시켜도 됨
            per.append([i,stages.count(i)/num*100])
        else:
            per.append([i,0])
    per.sort(key=lambda x:x[1], reverse=True)
    for i in per:
        answer.append(i[0])
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])

#답안
def solution(N, stages):
    answer = []
    par = len(stages)
    per = []
    for i in range(1,N+1):
        level = stages.count(i)
        if par > 0:
            per.append([i,level/par])
        else:
            per.append([i,0])
        par -= level
    per.sort(key=lambda x:x[1], reverse=True)
    for i in per:
        answer.append(i[0])
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])