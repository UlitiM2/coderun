a = int(input())
b = int(input())
n = int(input())
m = int(input())

min1 = (n - 1) * (a + 1) + 1
max1 = (n + 1) * (a + 1) - 1

min2 = (m - 1) * (b + 1) + 1
max2 = (m + 1) * (b + 1) - 1

overall_min = max(min1, min2)
overall_max = min(max1, max2)

if overall_min > overall_max:
    print(-1)
else:
    print(overall_min, overall_max)
