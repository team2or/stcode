#1,2,3 더하기
import sys
def solution():
    global t
    global ns
    t=int(sys.stdin.readline())
    ns=[0]*11

    ns[1]=1
    ns[2]=2
    ns[3]=4

    for i in range(4,11):
        ns[i]= sum(ns[i-3:i])
    
    
    return ns, t

if __name__=="__main__":
    ans=solution()
    for _ in range(t):
        print(ns[int(sys.stdin.readline())])