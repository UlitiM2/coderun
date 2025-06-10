n = int(input())
mass_ch = []
for _ in range(n):
    mass_ch.append(input().split())

left = 30
right = 4000
curr_ch = 0
previous_ch = float(mass_ch[0][0])

for i in range(1, n):
    curr_ch = float(mass_ch[i][0])
    curr_type = mass_ch[i][1]
    if curr_ch == previous_ch:
        continue
    if curr_type == 'closer':
        if curr_ch > previous_ch:
            left = max(left, (previous_ch+curr_ch) / 2)
        else:
            right = min(right, (previous_ch+curr_ch) / 2)
    elif curr_type == 'further':
        if curr_ch > previous_ch:
            right = min(right, (previous_ch+curr_ch) / 2)
        else:
            left = max(left, (previous_ch+curr_ch) / 2)
    previous_ch = curr_ch

print(round(left, 6), round(right, 6))
