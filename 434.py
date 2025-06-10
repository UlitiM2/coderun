def find_partitions(n):
    def backtrack(max_num, remaining, path, result):
        if remaining == 0:
            result.append(path.copy())
            return
        for num in range(min(max_num, remaining), 0, -1):
            path.append(num)
            backtrack(num, remaining - num, path, result)
            path.pop()

    result = []
    backtrack(n, n, [], result)
    return result


n = int(input())
partitions = find_partitions(n)
for partition in reversed(partitions):
    print(" + ".join(map(str, partition)))
