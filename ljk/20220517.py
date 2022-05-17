#20220517
def solution(skill, skill_trees):
    skill = list(skill)
    cnt = 0
    for skill_tree in skill_trees:
        bag = skill[:]
        for i in skill_tree:
            if i not in bag:
                pass
            elif i == bag[0]:
                bag.pop(0)
            else:
                break
            if len(bag) == 0 or skill_tree[len(skill_tree)-1]==i:
                cnt+=1
                break
    return cnt
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))