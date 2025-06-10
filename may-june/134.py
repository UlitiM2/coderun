n = int(input())
counts = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
else:
    total = 0
    for i in range(n - 1):
        total += min(counts[i], counts[i + 1])
    print(total)
