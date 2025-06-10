n = list(map(int, input().split()))
N = input()

count = 0
for i in N:
    if int(i) not in n:
        count += 1
        n.append(int(i))
print(count)
