n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))
count_kl = {}

for i in range(k):
    if p[i] not in count_kl:
        count_kl[p[i]] = 1
    else:
        count_kl[p[i]] += 1

for j in range(1, n+1):
    if j in count_kl and c[j-1] >= count_kl[j]:
        print("NO")
    else:
        print("YES")
