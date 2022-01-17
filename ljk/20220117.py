#수박수박수박
def solution(n):
    answer = ''
    su='수'
    bak='박'
    for i in range(n):
        if i%2==0:
            answer+=su
        else:
            answer+=bak
    return answer

def solution(n):
    return "수박"*(n//2) + "수"*(n%2)

def solution(n):
    return ("수박"*n)[0:n]


#키패드 누르기

(-1,3) (1,0) L
1, 4
(0,3) (1,0) L



def solution(n, hand):
    answer=''
    position={'left':(-1,0),'right':(1,0)}
    graph={0:(0,0), 8:(0,1),5:(0,2),2:(0,3),
            '*':(-1,0), 7:(-1,1),4:(-1,2),1:(-1,3),
            '#':(1,0),9:(1,1),6:(1,2),3:(1,3)}
    for i in n:
        if i in [1,4,7]:
            position['left']=graph[i]
            answer+='L'
        elif i in [3,6,9]:
            position['right']=graph[i]
            answer+='R'
        else:     
            l_distance=abs(graph[i][0]-position['left'][0])+abs(graph[i][1]-position['left'][1])
            
            r_distance=abs(graph[i][0]-position['right'][0])+abs(graph[i][1]-position['right'][1])
           
            
            if l_distance < r_distance:
                position['left']=graph[i]
                answer+='L'
            elif r_distance < l_distance:
                position['right']= graph[i]
                answer+='R'
            else:
                if hand=='left':
                    position['left']=graph[i]
                    answer+='L'
                else:
                    position['right']=graph[i]
                    answer+='R'
    return answer
            
                
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'left')


