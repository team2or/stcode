#주차요금계산
from collections import deque
import math
def solution(fees, records):
    answer = []
    base_time, base_fee, extra_time, extra_fee = fees

    dic = dict()
    for info in records:
        times, car_number, inAndOut = info.split()
        car_number = int(car_number)

        if car_number in dic:
            dic[car_number].append([toMinutes(times), inAndOut])
        else:
            dic[car_number] = [[toMinutes(times), inAndOut]]

    rList = list(dic.items())
    rList.sort(key=lambda x: x[0])
    for r in rList:
        t = 0

        for rr in r[1]:
            if rr[1] =="IN":
                t -= rr[0]
            else:
                t += rr[0]
        if r[1][-1][1] == 'IN':
            t += toMinutes("23:59")

        if t <= base_time:
            answer.append(base_fee)

        else:
            answer.append(base_fee + math.ceil((t-base_time)/ extra_time)*extra_fee)
    return answer

def toMinutes(times):
    h, m = map(int, times.split(':'))
    return h*60+ m



solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])