#1
lenth = int(input())
num = input()
total = []
for i in range(lenth):
    total.append(int(num[i]))
print(sum(total))

#2
lenth = int(input())
num = input()
total = 0
for i in range(lenth):
    total += int(num[i])
print(total)