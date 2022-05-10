#프로그래머스_SQL
#복습
#없어진 기록 찾기
#https://programmers.co.kr/learn/courses/30/lessons/59042
SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_OUTS OUTS LEFT JOIN ANIMAL_INS INS ON INS.ANIMAL_ID=OUTS.ANIMAL_ID
WHERE INS.DATETIME IS NULL ORDER BY OUTS.ANIMAL_ID;

#숫자의표현
#https://programmers.co.kr/learn/courses/30/lessons/12924
#내답안: 효율성에서 시간초과 뜸
n = 15
#자기자신 포함해야하므로 기본값 1로 설정
answer = 0
num_list = []
for i in range(1,n+1):
    num_list.append(i)
for i in range(n):
    #n/2한 수 이상일 때는 자기자신을 제외
    #연속된 수의 합이 n이상일 수 밖에 없음
    if n/2 < i:
        break
    else:
        sum_num = 0
        for num in num_list[i:]:
            sum_num += num
            if sum_num == n:
                answer += 1
                break
            elif sum_num > n:
                break
print(answer+1)
#수정참고
#https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9CLevel-2
n = 15
#자기자신 포함해야하므로 기본값 1로 설정
answer = 1
for i in range(1,n+1):
    #n/2한 수 이상일 때는 자기자신을 제외
    #연속된 수의 합이 n이상일 수 밖에 없음
    if n/2 < i:
        break
    else:
        sum_num = 0
        for num in range(i,n+1):
            sum_num += num
            if sum_num == n:
                answer += 1
                break
            elif sum_num > n:
                break
print(answer)

#Java
#두수비교하기
#https://www.acmicpc.net/submit/1330
#참고: https://st-lab.tistory.com/21
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        sc.close();
        if (A > B){
            System.out.println(">");
        } else if (A < B) {
            System.out.println("<");
        } else {
            System.out.println("==");
        }
    }
}
