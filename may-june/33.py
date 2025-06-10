first_string = input().strip()
second_string = input().strip()
len_first = len(first_string)
len_second = len(second_string)

dp = [[0] * (len_second + 1) for _ in range(len_first + 1)]
for i in range(len_first + 1):
    dp[i][0] = i
for j in range(len_second + 1):
    dp[0][j] = j
for i in range(1, len_first + 1):
    for j in range(1, len_second + 1):
        if first_string[i - 1] == second_string[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
print(dp)
print(dp[len_first][len_second])
