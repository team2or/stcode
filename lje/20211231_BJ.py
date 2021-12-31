#baekjoon
#문제1_더하기 사이클
#https://www.acmicpc.net/problem/1110

def solution(n):
    if n < 10:
        n = str(0)+str(n)
        num_list = [n[0], n[1]]
        new = ''
        no = 0
        while str(n) != str(new):
            if len(str(int(num_list[0])+int(num_list[1]))) > 1:
                new = num_list[1] + str(int(num_list[0])+int(num_list[1]))[1]
                num_list = [str(new)[0], str(new)[1]]
            else:
                new = num_list[1] + str(int(num_list[0])+int(num_list[1]))
                num_list = [str(new)[0], str(new)[1]]
                no += 1
    else:
        num_list = [str(n)[0], str(n)[1]]
        new = ''
        no = 0
        while str(n) != str(new):
            if len(str(int(num_list[0])+int(num_list[1]))) > 1:
                new = num_list[1] + str(int(num_list[0])+int(num_list[1]))[1]
                num_list = [str(new)[0], str(new)[1]]
                no += 1
            else:
                new = num_list[1] + str(int(num_list[0])+int(num_list[1]))
                num_list = [str(new)[0], str(new)[1]]
                no += 1
    print(no)
n = int(input())
solution(n)

#문제2_숫자의 합
#https://www.acmicpc.net/problem/11720
n = input()
num = input()
answer = 0
for i in str(num):
    answer += int(i)
print(answer)

n = '00'
print(n[0])