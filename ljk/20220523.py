def solution(s):
    strlist = []
    for i in s:
        if len(strlist) >0 and strlist[-1]==i:
            strlist.pop()
        else:
            strlist.append(i)
    if strlist:
        return 0
    else:
        return 1