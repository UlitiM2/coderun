n, k = map(int, input().split())
N = list(map(int, input().split()))
K = list(map(int, input().split()))


def find_close(mass, num):
    left = 0
    right = len(mass) - 1
    while left < right:
        mid = (left + right) // 2
        if mass[mid] < num:
            left = mid + 1
        else:
            right = mid

    if left == 0:
        return mass[0]
    if abs(mass[left-1] - num) <= abs(mass[left] - num):
        return mass[left-1]
    else:
        return mass[left]


for i in range(k):
    print(find_close(N, K[i]))

