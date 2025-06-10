N, M = map(int, input().split())
colors_for_Anna = set()
colors_for_Boris = set()

for _ in range(N):
    colors_for_Anna.add(int(input()))
for _ in range(M):
    colors_for_Boris.add(int(input()))

all_colors = colors_for_Anna | colors_for_Boris
same_colors = set(colors_for_Anna & colors_for_Boris)
Anna_colors = all_colors - colors_for_Boris
Boris_colors = all_colors - colors_for_Anna

print(len(same_colors))
print(*sorted(same_colors), sep=' ')

print(len(Anna_colors))
print(*sorted(Anna_colors), sep=' ')

print(len(Boris_colors))
print(*sorted(Boris_colors), sep=' ')
