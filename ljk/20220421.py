#20220413
def connect(list, i, adj):
    stack = []
    for i in list:
        stack.append(i)
    visit = [0] * len(adj)
    visit[i - 1] = 1
    while stack:
        a = stack.pop()
        for i in adj[a - 1]:
            if not visit[i - 1]:
                stack.append(i)
                visit[i - 1] = 1
    return visit


def solution(n, wires):
    adj = [[] for _ in range(n)]

    for a, b in wires:
        adj[a - 1].append(b)
        adj[b - 1].append(a)

    min_v = 100

    for i in range(n):
        for j in range(len(adj[i])):
            tmp = adj[i][j]
            adj[i].remove(adj[i][j])
            if adj[i]:
                res = connect(adj[i], i, adj)
                min_v = min(min_v, abs(res.count(0) - res.count(1)))
            adj[i] = [tmp] + adj[i]
    return min_v