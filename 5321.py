k = int(input())
total_sum = 0
for i in range(1, k + 1):
    total_sum += 2 ** (i - 1)
print(total_sum)
