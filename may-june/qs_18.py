N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N + 1)
stack = [1]
visited[1] = True
component = []

while stack:
    u = stack.pop()
    component.append(u)
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            stack.append(v)

component.sort()
print(len(component))
print(' '.join(map(str, component)))
