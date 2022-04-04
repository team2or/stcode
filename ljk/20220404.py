#주식가격

def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        time= len(prices)-i-1
        for j in range(i+1, len(prices)):
            if prices[j]< prices[i]:
                time=j-i
                break
        answer.append(time)
    answer.append(0)
    return answer