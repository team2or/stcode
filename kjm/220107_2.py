# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjKXKALcDFAUq
# SW Expert Academy 1936.

N = input()
if int(N[0]) + int(N[2]) == 3:
    if N[0] == "2":
        print("A")
    else:
        print("B")
        
elif int(N[0]) + int(N[2]) == 5:
    if N[0] == "3":
        print("A")
    else:
        print("B")
        
elif int(N[0]) + int(N[2]) == 4:
    if N[0] == "1":
        print("A")
    else:
        print("B")