from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for num in course:
        array = []
        for order in orders:
            # 주문 문자열 정렬
            order = sorted(order) 
            # array에 현재 주문에서 num개를 뽑아 나올 수 있는 경우를 넣음
            array.extend(list(combinations(order, num)))
        
        # 카운터를 사용하여 중복되는 횟수를 셈
        count = Counter(array)
        
        if count:
            # 제일 많이 나온 조합이 두번 이상 시켜졌다면
            if max(count.values()) >= 2:
                for key, value in count.items():
                    # 현재 조합이 가장 많이 시켜졌다면 결과배열에 추가
                    if value == max(count.values()):
                        answer.append("".join(key))
    
    # 정렬하여 return 
    return sorted(answer)