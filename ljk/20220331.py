#비밀번호 찾기
from sys import stdin

class password:
    def __init(self):
        pass

    def sin(self,n,m):
        site={}
        for i in range(n):
            s,p=map(str,stdin.readline().rstrip().split())
            site[s]=p
        s_list=[]
        for j in range(m):
            wanted_s=stdin.readline().rstrip()
            s_list.append(wanted_s)
        answer=[site[i] for i in s_list]
        return answer
if __name__=="__main__":
    n,m=map(int,stdin.readline().split())
    ans=password()
    for i in ans.sin(n,m):
        print(i)


    

  