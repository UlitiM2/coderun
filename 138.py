N, M, K = map(int, input().split())

matrix = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, M + 1):
        matrix[i][j] = row[j - 1]

prefix = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = matrix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

output = []
for _ in range(K):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    res = prefix[x_2][y_2] - prefix[x_1-1][y_2] - prefix[x_2][y_1-1] + prefix[x_1-1][y_1-1]
    output.append(str(res))

print('\n'.join(output))
