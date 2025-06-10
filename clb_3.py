n = int(input())
a = list(map(int, input().split()))
sum_percent = 0
for i in range(n):
    sum_percent += a[i]
count_hours = 100 // sum_percent
print(count_hours)
