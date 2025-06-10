import math


def minimal_board_size(n, w, h):
    min_side = math.isqrt(n * w * h)
    if min_side * min_side < n * w * h:
        min_side += 1

    max_side = n * max(w, h)

    left = min_side
    right = max_side
    answer = max_side

    while left <= right:
        mid = (left + right) // 2
        diplomas_per_row = mid // w
        if diplomas_per_row == 0:
            left = mid + 1
            continue
        rows = (n + diplomas_per_row - 1) // diplomas_per_row
        total_height = rows * h
        if total_height <= mid:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


w, h, n = map(int, input().split())
print(minimal_board_size(n, w, h))
