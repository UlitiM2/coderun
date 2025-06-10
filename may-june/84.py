n = int(input())
uniq_w = {}

for _ in range(n):
    w, h = map(int, input().split())
    if w not in uniq_w:
        uniq_w[w] = h
    else:
        if uniq_w[w] < h:
            uniq_w[w] = h

total_high = sum(uniq_w.values())
print(total_high)
