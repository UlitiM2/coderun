from collections import deque
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

result = []

dq = deque()

for i in range(n):
    while dq and dq[0] <= i - k:
        dq.popleft()

    while dq and numbers[dq[-1]] >= numbers[i]:
        dq.pop()

    dq.append(i)
    if i >= k - 1:
        result.append(numbers[dq[0]])

print('\n'.join(map(str, result)))
