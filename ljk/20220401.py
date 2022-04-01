#완주하지 못한 선수
from sys import stdin

class fashion:
    def __init(self):
        pass

    def sin(self,t):
        ans = []
        for _ in range(t):
            n=int(stdin.readline())
            items={}

            for i in range(n):
                cloth, type=map(str, stdin.readline().split())
                value=items.get(type)
                if value!=None:
                    items[type].append(cloth)
                else:
                    items[type]=[cloth]
                if '' not in items[type]:
                    items[type].append('')
            cnt=1
            for i in items.keys():
                cnt*=len(items[i])
            ans.append(cnt-1)
        return ans

if __name__=="__main__":
    t=int(stdin.readline())
    ans=fashion()
    for i in ans.sin(t):
        print(i)


    

  