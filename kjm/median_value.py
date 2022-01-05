N = int(input())
score = input().split(" ")
score.sort()
print(score[(N//2)-2])