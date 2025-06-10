n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

dp = [[0] * m for _ in range(n)]
max_size = 0
max_i, max_j = 0, 0

for i in range(n):
    dp[i][0] = grid[i][0]
    if dp[i][0] > max_size:
        max_size = dp[i][0]
        max_i, max_j = i, 0
for j in range(m):
    dp[0][j] = grid[0][j]
    if dp[0][j] > max_size:
        max_size = dp[0][j]
        max_i, max_j = 0, j

for i in range(1, n):
    for j in range(1, m):
        if grid[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            if dp[i][j] > max_size:
                max_size = dp[i][j]
                max_i, max_j = i, j

top_left_i = max_i - max_size + 1
top_left_j = max_j - max_size + 1

print(max_size)
print(top_left_i + 1, top_left_j + 1)
