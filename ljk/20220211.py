def solution(s):

    sl = []

    for i in s:
        if len(sl) > 0 and sl[-1] == i:
            sl.pop()
        else:
            sl.append(i)
    if sl:
        return 0
    else:
        return 1