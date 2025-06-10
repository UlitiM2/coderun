N = int(input())
mass = list(map(int, input().split()))
x = int(input())

num = float('inf')
difference = float('inf')
for i in range(N):
    if abs(x - mass[i]) < difference:
        num = mass[i]
        difference = abs(x - mass[i])

print(num)
