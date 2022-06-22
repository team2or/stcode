import sys

k = int(sys.stdin.readline())
num_stack = []

for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        del num_stack[-1]
    else:
        num_stack.append(num)

if num_stack:
    print(sum(num_stack))
else:
    print(0)