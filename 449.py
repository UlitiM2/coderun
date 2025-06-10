n = int(input())
a = list(map(int, input().split()))
X = int(input())
b = list(map(int, input().split()))
k = int(input())
c = list(map(int, input().split()))

index_to_price = {i+1: a[i] for i in range(n)}

from collections import defaultdict
count = defaultdict(int)
for item in c:
    count[item] += 1

combo_items = b
combo_price = X

individual_combo_cost = sum(index_to_price[item] for item in combo_items)

if individual_combo_cost <= combo_price:
    total = sum(count[item] * index_to_price[item] for item in count)
else:
    max_t = max(count.get(item, 0) for item in combo_items) + 1
    min_total = float('inf')
    for t in range(0, max_t + 1):
        current_cost = t * combo_price
        for item in combo_items:
            current_cost += max(count.get(item, 0) - t, 0) * index_to_price[item]
        for item in count:
            if item not in combo_items:
                current_cost += count[item] * index_to_price[item]
        if current_cost < min_total:
            min_total = current_cost
    total = min_total

print(total)
