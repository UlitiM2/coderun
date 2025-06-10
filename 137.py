K = int(input())
X = []
Y = []
for _ in range(K):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

min_x = min(X)
max_x = max(X)

min_y = min(Y)
max_y = max(Y)
print(min_x, min_y, max_x, max_y)
