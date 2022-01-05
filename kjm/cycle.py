T = int(input())
for i in range(1, T+1):
    text = input()
    for j in range(1, 11):
        if text[:j] == text[j:j+j]:
            break
    print(f"#{i} {j}")