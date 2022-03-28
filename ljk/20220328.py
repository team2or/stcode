#수찾기
from sys import stdin,stdout
from collections import deque
class Cycle:
    def __init__(self):
        n= int(stdin.readline())
        # ns=set(map(int, stdin.readline().split()))
        ns=sorted(list(map(int, stdin.readline().split())))
        m= int(stdin.readline())
        ms=list(map(int, stdin.readline().split()))
        # for l in ms:
        #     stdout.write('1\n') if l in ns else stdout.write('0\n')

        for i in range(len(ms)):
            print(self.binary(ms[i], ns))
    def binary(self, element, list, start=0, end=None):

        if end==None:
            end=len(list)-1
        if start > end:
            return 0
        mid = (start+end)//2

        if element== list[mid]:
            return 1
        elif element < list[mid]:
            end=mid-1
        elif element> list[mid]:
            start= mid+1
        return self.binary(element, list, start, end)
if __name__=="__main__":
    Cycle() 
  