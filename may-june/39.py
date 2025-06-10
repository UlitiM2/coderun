v, r = map(int, input().split())

graph = {}

for _ in range(r):
    start, end = map(int, input().split())
    if end not in graph:
        graph[end] = [start]
    else:
        graph[end].append(start)

visited = set()
stack = [1]

while stack:
    point = stack.pop()

    if point not in visited:
        visited.add(point)

        for neighbour in graph.get(point, []):
            if neighbour not in visited:
                stack.append(neighbour)


print(*sorted(visited))
