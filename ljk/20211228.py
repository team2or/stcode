def solution(n):
    answer=[]
    li=list(str(n))
    for i in range(len(li)):
        int_=li.pop()
        answer.append(int(int_))    
    return answer

solution(12345)

a=[1,2,3,4,5]
a=reversed(a)
list(a)

n=12345
n = str(n)
answer = [int(i) for i in n]
answer
list(reversed(answer))
#리스트를 뒤집을 때는 reversed(리스트)
#그리고 리스트로 덮어줘야한다.




def weekday(a,b):
    import calendar
    integer=calendar.weekday(2016,a,b) #0~6 인덱스 값 반환
    week=['MON','TUE','WED','THU','FRI','SAT','SUN']
    return week[integer]

weekday(5.24)

def solution(a,b):
    answer=''
    day=

def solution(a, b):
    answer = ''
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    count = 0

    for i in range(1, a):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            b += 31
        elif i in [4,6,9,11]:
            b += 30
        elif i == 2:
            b += 29
    print(b)
    count += b
    print(count)
    answer = day[count%7-1]
    return answer
solution(1,1)

for i in range(1,1):
    print(i)