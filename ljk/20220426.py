''' 자릿수 더하기''

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    return answer;
}

int solution(int n) {
    int answer = 0;
    while(n!=0)
    {
        answer+=n%10;
        n/=10; //객주달기는 //
    }
    return answer;
}
'''
#오픈채팅방

def solution(record):
    answer = []
    user_db = dict()
    actions = []
    for event in record:
        info = event.split()
        action, id = info[0], info[1]
        if action in ('Enter', 'Change'):
            nickname = info[2]
            user_db[id] = nickname
        actions.append((action, id))

    for actionInfo in actions:
        action, id = actionInfo[0], actionInfo[1]
        if action == 'Enter':
            answer.append(f"{user_db[id]}님이 들어왔습니다.")
        elif action == 'Leave':
            answer.append(f'{user_db[id]}님이 나갔습니다.')

    return answer

a= solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(a)