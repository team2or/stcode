#해커랭크
#복습
#Ollivander's Inventory
#https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
SELECT W.id, WP.age, W.coins_needed, W.power FROM Wands W LEFT JOIN Wands_Property WP ON W.code = WP.code WHERE W.coins_needed = (SELECT min(W1.coins_needed) FROM Wands W1 LEFT JOIN Wands_Property WP1 ON W1.code=WP1.code WHERE WP1.is_evil = 0 AND W.power = W1.power AND WP.age=WP1.age) ORDER BY W.power DESC, WP.age DESC; 

#프로그래머스
#올바른 괄호
#https://programmers.co.kr/learn/courses/30/lessons/12909
s= "()()"
s= "(())()"
s=")()("
def solution(s):
    s_list = []
    for i in s:
        if len(s_list) > 0:
            if s_list[-1] == "(" and i == ")":
                s_list.pop()
            else:
                s_list.append(i)
        else:
            s_list.append(i)
    if len(s_list) == 0:
        return True
    else:
        return False
solution(s)