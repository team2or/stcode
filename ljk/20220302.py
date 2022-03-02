# 소수찾기
import itertools

from itertools import combinations, permutations
import math
k="011"
def powerset(iter):
    powerset_=[]
    for i in range(1,len(iter)+1):
        for j in permutations(iter, i):
            if list(j)[0]==0:
                pass
            else:
                powerset_.append(list(j))
    return powerset_

def T_F(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number%i ==0:
            return False
    return True

def solution(k):
    answer=0
    nums=[]
    for i, combo in enumerate(powerset(k), 1):
        if combo:
            num=int(''.join(list(combo)))
            if num not in nums:
                nums.append(num)
    for j in nums:
        if j!=1 and j!=0:
            if T_F(j)==True:
                answer+=1   
    return answer
        