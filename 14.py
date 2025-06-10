import sys


def bfs(destination, n, m):
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    queue = [(destination[0], destination[1], 0)]
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[destination[0]][destination[1]] = 0
    
    while queue:
        x, y, dist = queue.pop(0)
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = dist + 1
                    queue.append((nx, ny, dist + 1))
    return visited


data = list(map(int, input().split()))
N, M, S, T, Q = data[0], data[1], data[2], data[3], data[4]
S -= 1
T -= 1
total_sum = 0
possible = True
visited = bfs((S, T), N, M)

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if visited[x][y] == -1:
        print(-1)
        sys.exit()
    else:
        total_sum += visited[x][y]

print(total_sum)
