import sys


def bfs(start, n, matrix):
    directions = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1)]
    queue = [(start[0], start[1], start[2], 0)]
    visited = set()

    while queue:
        z, x, y, dist = queue.pop(0)

        if z == 0:
            return dist

        for dz, dx, dy in directions:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if 0 <= nx < n and 0 <= ny < n and 0 <= nz < n:
                if (nz, nx, ny) not in visited and matrix[nz][nx][ny] != '#':
                    visited.add((nz, nx, ny))
                    queue.append((nz, nx, ny, dist + 1))
    return -1

sys.stdin = open('file_for_15.txt')
data = sys.stdin.readlines()
n = int(data[0].strip())
matrices = []
curr_matrix = []

for line in data[2:]:
        stripped_line = line.strip()
        if not stripped_line:
            if curr_matrix:
                matrices.append(curr_matrix)
                curr_matrix = []
        else:
            row = list(stripped_line)
            curr_matrix.append(row)
            if 'S' in row:
                Z, X, Y = len(matrices), len(curr_matrix) - 1, row.index('S')
if curr_matrix:
    matrices.append(curr_matrix)

print(bfs((Z, X, Y), n, matrices))


