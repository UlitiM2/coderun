n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[1][1] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            continue
        if i - 2 >= 1 and j - 1 >= 1:
            dp[i][j] += dp[i - 2][j - 1]
        if i - 1 >= 1 and j - 2 >= 1:
            dp[i][j] += dp[i - 1][j - 2]

print(dp[n][m])
