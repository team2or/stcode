
#별채우기
for i in range(5):
    str_=['+']*5
    str_[i]='#'
    print(''.join(str_))

for i in range(5):
    for j in range(5):
        if i==j:
            print('#',end='')
        else:
            print('+',end='')
    print()

print("#++++")
print("+#+++")
print("++#++")
print("+++#+")
print("++++#")

#패턴 마디의 길이

T=int(input())
for i in range(T):
    t=input()
    for j in range(1,11):
        if t[:j]==t[j:j*2]j:
            print('#{i+1} {j}')
            break

    