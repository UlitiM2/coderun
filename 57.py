str_1 = str(input())
str_2 = str(input())

pair_counts = {}
for i in range(len(str_2) - 1):
    pair = str_2[i:i+2]
    pair_counts[pair] = pair_counts.get(pair, 0) + 1

count = 0
for j in range(len(str_1) - 1):
    if str_1[j:j+2] in pair_counts:
        count += 1
print(count)
