def solution(lottos, win_nums):
    answer = []
    cnt = 0
    luck_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            cnt += 1
        elif lotto in win_nums:
            luck_cnt += 1
    award = dict()
    for i in range(6):
        award[i+1] = 6-i
    award[0] = 6
    return [award[cnt+luck_cnt], award[luck_cnt] ]