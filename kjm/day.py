from datetime import datetime
def solution(a, b):
    try:
        date = f'2016-{a}-{b}'
        datetime_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("해당 일자가 존재하지 않습니다.")
    else:
        dateDict = {0: 'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
        answer = dateDict[datetime_date.weekday()]
        return answer