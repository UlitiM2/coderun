def generate_partitions(n):
    def suma_obj(remaining, max_part, path, mass_result):
        if remaining == 0:
            mass_result.append(" + ".join(map(str, path)))
            return
        for x in range(min(max_part, remaining), 0, -1):
            suma_obj(remaining - x, x, path + [x], mass_result)
    
    result = []
    suma_obj(n, n, [], result)
    return result


N = int(input())
partitions = generate_partitions(N)
for partition in partitions[::-1]:
    print(partition)
