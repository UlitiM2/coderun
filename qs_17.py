N, M, K = map(int, input().split())
field = [[0 for _ in range(M)] for _ in range(N)]
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]
for i in range(K):
    p, q = map(int, input().split())
    field[p-1][q-1] = '*'

    for j, k in directions:
        new_j, new_k = (p-1) + j, (q-1) + k
        if (0 <= new_j < N) and (0 <= new_k < M) and (field[new_j][new_k] != '*'):
            field[new_j][new_k] += 1

for row in field:
    print(' '.join(map(str, row)))
