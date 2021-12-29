def solution(a,b):
    answer=[]
    store=[]
    b_=b
    a_=a
    for i in range(2,b+1):
        while a_%i==0 and b_%i==0:
            store.append(i)
            a_=a_/i
            b_=b_/i
    if len(store)==0:
        store.append(1)
    ans=1
    for i in store:
        ans*=i
    answer.append(ans)
    answer.append(round(a*b/answer[0]))
    return answer

solution(5,4)

def solution(a,b):
    mod=a%b
    a_=a;b_=b
    while mod> 0:
        a_, b_ = b_, mod
        mod=a_%b_
    mut=round(a*b/b_)
    return [b_,mut]
    
solution(2,3)

def solution(s):
    return_=[]
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    count1=0
    count2=0
    count3=0
    for idx, answer in enumerate(s):
        if answer== a1[idx%len(a1)]:
            count1+=1
        if answer == a2[idx%len(a2)]:
            count2+=1
        if answer== a3[idx%len(a3)]:
            count3+=1
    num=[count1, count2, count3]
    print(num)
    for idx , counting in enumerate(num):
        if max(num)== num[idx]:
            return_.append(idx+1)
    return return_

solution([1,2,3,4,5])

num=[5,0,0]
num.append(1)
num