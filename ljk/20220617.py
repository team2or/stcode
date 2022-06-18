def solution(s):
    d = dict()
    for i in range(65, 91):
        d[chr(i)] = i-64

    start = 0
    end = len(s)
    r = []

    while True:
        a = s[start:end]
        if a in d.keys():
           r.append(d[a])

           if end>=len(s):
                return r

           d[a+s[end]] = max(d.values())+1
           start += len(a)
           end = len(s)

        else:
            end -= 1

solution('KAKAO')
