#영어 끝말잇기
import math
def solution(n, words):
    answer=[0,0]
    for word in words[:-1]:
        index=words.index(word)
        if words[index+1] in words[:index]:
            answer[1]=math.ceil((index+2)/n)
            if (index+2)%n==0:
                answer[0]=n
            else:
                answer[0]=(index+2)%n
            break
        elif words[index][-1]==words[index+1][0]:
            pass
        else:
            answer[1]=math.ceil((index+2)/n)
            if (index+2)%n==0:
                answer[0]=n
            else:
                answer[0]=(index+2)%n
            break
    return answer

solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])


def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]
