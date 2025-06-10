N, K = map(int, input().split())
all_lens = []
for _ in range(N):
    L = int(input())
    all_lens.append(L)


def binary_search(lens, parts):
    left = 1
    right = max(lens)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        count_parts = 0
        for i in lens:
            count_parts += (i // mid)

        if count_parts >= parts:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(binary_search(all_lens, K))
