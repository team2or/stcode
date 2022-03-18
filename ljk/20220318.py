#거꾸로 구구단 

# import sys
# def solution():
#     answer='0'
#     n,k = map(int, sys.stdin.readline().split())
#     maxlen= len(str(n*k))

#     for i in range(1,k+1):
#         if len(str(i*n))== maxlen:
#             no=str(i*n)
#             if int(no[-1]) >= int(answer[0]):
#                 if len(no)%2!=0:
#                     j=len(no)//2
#                     if j==0:
#                         if int(answer)< int(no):
#                             answer=no
#                     else:
#                         for r in range(1,j+1):
#                             no=list(no)
#                             no[j+r],no[j-r]=no[j-r],no[j+r]
#                             no=''.join(no)
#                             if int(answer)<int(no):
#                                 answer=no
#                 else:
#                     for j in range(maxlen//2):
#                         no=list(no)
#                         no[j],no[maxlen-1-j]= no[maxlen-1-j], no[j]
#                         no=''.join(no)
#                         if int(answer)<int(no):
#                             answer=no
#     return int(answer)


# if __name__=="__main__":
#     hats=solution()
#     print(hats)

import sys
class solution:
    def __init__(self):
        self.n, self.k = map(int,sys.stdin.readline().split())
        self.answer()
    def answer(self):
        maxlen=len(str(self.n*self.k))
        answer = [int(str(i*self.n)[::-1]) for i in range(1,self.k+1) if len(str(i*self.n)) >= maxlen]
        answer.sort()
        print(answer[-1])

if __name__=="__main__":
    solution()