mass = list(map(int, input().split()))
count = 0
for i in range(1, len(mass) - 1):
    if mass[i-1] < mass[i] > mass[i+1]:
        count += 1
print(count)
