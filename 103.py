n, m, k, p = map(int, input().split())

mass = [[n + k, max(m, p)], [m + p, max(n, k)], [n + p, max(m, k)], [m + k, max(n, p)]]
mass_square = [[int(i[0]) * int(i[1])] for i in mass]

min_size_idx = mass_square.index(min(mass_square))
print(*mass[min_size_idx])
