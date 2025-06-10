N = int(input())
n = sorted(set(map(int, input().split())))
K = int(input())
k = list(map(int, input().split()))


def binary_search(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


for i in range(K):
    count = binary_search(n, k[i])
    print(count)

