def bfs(start, destination):
    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)

        if current == destination:
            return path

        neighbors = []

        s = str(current).zfill(4)
        if s[0] != '9':
            new_num = int(str(int(s[0]) + 1) + s[1:])
            neighbors.append(new_num)

        if s[-1] != '1':
            new_num = int(s[:-1] + str(int(s[-1]) - 1))
            neighbors.append(new_num)

        rotated_right = int(s[-1] + s[:-1])
        neighbors.append(rotated_right)

        rotated_left = int(s[1:] + s[0])
        neighbors.append(rotated_left)

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return -1


start_point = int(input())
end_point = int(input())
print(*bfs(start_point, end_point), sep='\n')
