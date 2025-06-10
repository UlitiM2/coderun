N = int(input())
positions = []
for _ in range(N):
    pos = input().split()
    if pos[0] not in positions:
        positions.append(pos[0])

print(len(positions))
