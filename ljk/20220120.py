#실패율 

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])
def solution(n,stages):
    result={}
    length=len(stages)
    for stage in range(1,n+1):
        if length!=0:
            count= stages.count(stage)
            result[stage]=count/length
            length-=count
        else:
            result[stage]=0
    print(result)
    return sorted(result, key=lambda x :result[x],reverse=True)

a={1:'가가',2:'가다',3:'가나'}
sorted(a, key=lambda X: a[X],reverse=True)

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
#신고 결과받기
def solution(id_list, report, k):
    list_={}
    re_users=[]
    report=set(report)
    for i in report:
        user, re_user=i.split()
        if re_user not in list_:
            list_[re_user]=1
        else:
            list_[re_user]+=1
    for i,j in list_.items():
        if k<=j:
            re_users.append(i)
    answer=[0]*len(id_list)
    for q in report:
        user, re_user=q.split()
        if re_user in re_users:
            answer[id_list.index(user)]+=1
    return answer

    print(list_)

a={'frodo': 2, 'neo': 2, 'muzi': 1}
a[max(a)]
for i,j in a.items():
    if a[max(a)]==j:
        print(i)