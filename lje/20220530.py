#해커랭크
#복습
#Population Ceensus
SELECT sum(CITY.POPULATION) FROM CITY LEFT JOIN COUNTRY ON  CITY.CountryCode = COUNTRY.Code WHERE COUNTRY.CONTINENT = "Asia";

#프로그래머스
#메뉴리뉴얼
#https://programmers.co.kr/learn/courses/30/lessons/72411
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
from itertools import combinations
menu = {}
order_list = []
for order in orders:
    for i in range(2, len(order)+1):
        order_list.append(list(combinations(sorted(list(order)), i)))
order_list = sum(order_list,[])
for order in order_list:
    if len(order) in course:
        if ''.join(order) not in menu:
            menu[''.join(order)] = 1
        else:
            menu[''.join(order)] += 1
menu = sorted(list(menu.items()), key = lambda x:(len(x[0]),-x[1]))
answer = []
for k, v in menu:
    if v > 1:
        if len(answer) == 0:
            answer.append([k, v])
        elif len(answer) > 0 and len(answer[-1][0]) == len(k):
            if answer[-1][1] < v:
                answer.pop()
                answer.append([k, v])
            elif answer[-1][1] == v:
                answer.append([k, v])
        elif len(answer) > 0 and len(answer[-1][0]) != len(k):
            answer.append([k,v])
print(sorted([k for k, v in answer]))


#다른답안
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            #모든 조합을 구할필요 없이 course사이즈에 해당하는 조합만 구하면 됨
            order_combinations += itertools.combinations(sorted(order), course_size)

        #order_combinations 리스트에서 동일한 요소의 개수(빈도수.최빈값)를 반환
        most_ordered = collections.Counter(order_combinations).most_common()
        #개수가 2 이상이고 최빈값이 같은 메뉴는 추가해주기
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])

#[참고]
#.most_common(): 요소들의 빈도수(최빈값) 반환
#https://velog.io/@kimdukbae/Python-collections-%EB%AA%A8%EB%93%88%EC%9D%98-Counter