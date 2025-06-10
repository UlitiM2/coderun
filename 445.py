B, W = map(int, input().split())
size_near_wall = (B + 4) // 2

for m in range(2, size_near_wall // 2 + 1):
    n = size_near_wall - m
    if (n-2) * (m-2) == W:
        print(n, m)
        break
