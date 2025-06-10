N, K = input().split()
n = sorted(set(map(int, input().split())))
k = list(map(int, input().split()))


def binary_search(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] == x:
            return 'YES'
        else:
            right = mid
    return 'NO'


for j in k:
    print(binary_search(n, j))
