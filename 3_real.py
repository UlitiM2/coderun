N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            dp[i][j] = matrix[i][j]
        elif i == 0:
            dp[i][j] = matrix[i][j] + dp[i][j-1]
        elif j == 0:
            dp[i][j] = matrix[i][j] + dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
print(dp[-1][-1])

ans = []
i, j = N - 1, M - 1
while i > 0 or j > 0:
    if i == 0:
        ans.append('R')
        j -= 1
    elif j == 0:
        ans.append('D')
        i -= 1
    else:
        if dp[i - 1][j] > dp[i][j - 1]:
            ans.append('D')
            i -= 1
        else:
            ans.append('R')
            j -= 1
ans.reverse()
print(' '.join(ans))
