n = int(input())
count_goals = {}
for _ in range(n):
    name = input()
    count_goals[name] = 0

k = int(input())
prev_1, prev_2 = 0, 0

for _ in range(k):
    points, name = input().split()
    point_1, point_2 = map(int, points.split(':'))

    difference_1 = point_1 - prev_1
    difference_2 = point_2 - prev_2
    if difference_1 != 0:
        count_goals[name] += difference_1

    elif difference_2 != 0:
        count_goals[name] += difference_2

    prev_1, prev_2 = point_1, point_2

max_points = -1
best_player = None

for player, points in count_goals.items():
    if points > max_points:
        max_points = points
        best_player = player
    elif points == max_points:
        if player > best_player:
            best_player = player

print(best_player, max_points)
