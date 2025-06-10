n = int(input())
a = list(map(int, input().split()))
ans = [-1] * n
stack = []

for i in range(n):
    while stack and a[stack[-1]] > a[i]:
        ans[stack.pop()] = i
    stack.append(i)

print(' '.join(map(str, ans)))
