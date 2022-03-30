#듣보잡
from sys import stdin,stdout
from collections import deque
class Cycle:
    def __init__(self):
        n,m= map(int,stdin.readline().split())
        self.y_unknown=[]
        self.s_unknown=[]
        for i in range(n):
            self.y_unknown.append(stdin.readline().rstrip())
        for _ in range(m):
            self.s_unknown.append(stdin.readline().rstrip())
        self.sol()
    def sol(self):
        answer=list(set(self.y_unknown)&set(self.s_unknown))
        answer.sort()
        return(answer)





if __name__=="__main__":
    ans=Cycle().sol()
    print(len(ans))
    print(ans)
    for i in ans:
        if i:
            print(i)

  