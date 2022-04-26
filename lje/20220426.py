#프로그래머스
#복습/JOIN
#보호소에서 중성화한 동물
#https://programmers.co.kr/learn/courses/30/lessons/59045
SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME FROM ANIMAL_INS INS LEFT JOIN ANIMAL_OUTS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE INS.SEX_UPON_INTAKE LIKE "Intact%" AND OUTS.SEX_UPON_OUTCOME NOT LIKE "Intact%";

#2019 KAKAO BLIND RECRUITMENT
#오픈채팅방
#https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    names = {}
    chat = []
    for re in record:
        re = list(map(str, re.split()))
        if len(re) == 3:
            names[re[1]] = re[2]
            chat.append([re[1], re[0]])
        else:
            chat.append([re[1], re[0]])
    result = []
    for c in chat:
        if c[1] == "Enter":
            result.append(f"{names[c[0]]}님이 들어왔습니다.")
        elif c[1] == "Leave":
            result.append(f"{names[c[0]]}님이 나갔습니다.")
    return result

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

#Java
#자릿수 더하기
#https://programmers.co.kr/learn/courses/30/lessons/12931?language=java

#숫자->문자로 타입변환
#https://hianna.tistory.com/524
#문자열 나누기(하나씩 출력)
#https://coding-factory.tistory.com/73

import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        #숫자 -> 문자 변환
        String N = Integer.toString(n);
        #리스트 변수 선언
        String[] array_N;
        #문자열 하나씩 나눠 리스트에 담기
        array_N = N.split("");
        #리스트에서 문자열 하나씩 추출하여 더하기
        for (int i=0; i<array_N.length; i++){
            answer += Integer.parseInt(array_N[i]);
        }

        return answer;
    }
}
