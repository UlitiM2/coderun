mass = list(map(int, input().split()))
flag = 1
for i in range(len(mass) - 1):
    if mass[i] >= mass[i + 1]:
        flag = -1
        break

if flag == -1:
    print("NO")
else:
    print("YES")
