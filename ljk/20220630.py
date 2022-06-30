def solution(n):
    three=''
    while n>0:
        n,y=divmod(n,4)
        three+=str(y)
        print(n,y)
    return int(three,4)