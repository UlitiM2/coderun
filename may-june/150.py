n = int(input())

if n == 0:
    print(0)
else:
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 0

    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        dp[i][1] = dp[i-1][0]
        dp[i][2] = dp[i-1][1]

    total = dp[n][0] + dp[n][1] + dp[n][2]
    print(total)
