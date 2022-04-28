#20220428
from collections import deque
def solution(begin, target, words):
    queue = deque([(begin, words, 0)])

    while queue:
        for _ in range(len(queue)):
            word, words, count = queue.popleft()

            if word == target:
                return count

            for i, item in enumerate(words):
                cnt = 0
                for j in range(len(word)):
                    if word[j] == item[j]:
                        cnt += 1
                if cnt == len(item)-1:
                    queue.append((item, words[:i] + words[i + 1:], count + 1))

    return 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))