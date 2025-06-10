from collections import deque


def knight_bfs(start):
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    visited = [[-1 for _ in range(8)] for _ in range(8)]
    q = deque()
    x, y = start
    visited[x][y] = 0
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited


red, green = input().split()


def pos_to_coords(pos):
    col = ord(pos[0]) - ord('a')
    row = int(pos[1]) - 1
    return (col, row)


red_coords = pos_to_coords(red)
green_coords = pos_to_coords(green)

red_visited = knight_bfs(red_coords)
green_visited = knight_bfs(green_coords)

min_moves = float('inf')
for i in range(8):
    for j in range(8):
        if red_visited[i][j] != -1 and green_visited[i][j] != -1 and (red_visited[i][j] == green_visited[i][j]):
            current_max = max(red_visited[i][j], green_visited[i][j])
            if current_max < min_moves:
                min_moves = current_max

if min_moves == float('inf'):
    print(-1)
else:
    print(min_moves)
