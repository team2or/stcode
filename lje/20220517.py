#프로그래머스_SQL
#복습
#고양이와 개는 몇마리 있을까
#https://programmers.co.kr/learn/courses/30/lessons/59040
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE;


#스킬트리
#https://programmers.co.kr/learn/courses/30/lessons/49993
#답안
#https://kdgt-programmer.tistory.com/48
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
answer = 0
for skills in skill_trees:
    #skill_trees에 스킬이 있는지 확인
    #있으면 해당 스킬의 index skill_index 리스트에 추가
    skill_index = []
    for s in skills:
        if s in skill:
            skill_index.append(skill.index(s))
    #skill_index의 순서가 0번부터 차례인지 확인
    if skill_index == [i for i in range(len(skill_index))]:
        answer += 1
print(answer)


#다른답안1
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer

#다른답안2
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer