#컵홀더

n= int(input())
seats=input().upper()
cups=''
cnt=0
for seat in seats:
    if seat== 'S':
        if cups:
           if cups[-1]=='*':
                cups+='*'
                cnt+=1
        else:
            cups+='*'*2
    elif seat=='L':
        if cups:
            if cups[-1]=='*':
                cups+=' '
                cnt+=1
            elif cups[-1]==' ':
                cups+='/'
            elif cups[-1]=='/':
                cups+='*'
print(cnt)