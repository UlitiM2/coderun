n, m, k = map(int, input().split())

matrix_A = []
for i in range(int(n)):
    matrix_A.append(list(map(int, input().split())))

matrix_B = []
for i in range(int(m)):
    matrix_B.append(list(map(int, input().split())))

matrix_res = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            matrix_res[i][j] += matrix_A[i][l] * matrix_B[l][j]

matrix_res_t = [[0 for _ in range(len(matrix_res))] for _ in range(len(matrix_res[0]))]
for i in range(len(matrix_res)):
    for j in range(len(matrix_res[0])):
        matrix_res_t[j][i] = matrix_res[i][j]

for row in matrix_res_t:
    print(' '.join(map(str, row)))
