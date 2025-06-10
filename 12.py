def bfs(start, destination, matrix):
    queue = [(start, 0)]
    visited = set()
    while queue:
        point, count = queue.pop(0)
        if point == destination:
            return count
        for i in range(0, len(matrix)):
            if (int(matrix[point-1][i]) == 1) and ((i+1) not in visited):
                queue.append((i+1, count+1))
                visited.add(i+1)
    return -1


N = int(input())
matrix_1 = [list(map(int, input().split())) for _ in range(N)]
start_point, destination_point = map(int, input().split())
print(bfs(start_point, destination_point, matrix_1))
