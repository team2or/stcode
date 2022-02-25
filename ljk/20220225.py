#컵홀더

n= int(input())
seats=input().upper()
cups=''
for seat in seats:
    if seat== 'S':
        if cups:
           if cups[-1]=='*':
                cups+='*'
        else:
            cups+='*'*2
    elif seat=='L':
        if cups:
            if cups[-1]=='*':
                cups+=' '
            elif cups[-1]==' ':
                cups+='/'
            elif cups[-1]=='/':
                cups+='*'
print(cups.count('*'))
