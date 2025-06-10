first_player = list(map(int, input().split()))
second_player = list(map(int, input().split()))

count_try = 0
while len(first_player) != 0 and len(second_player) != 0:
    count_try += 1
    if count_try > 10 ** 6:
        print("botva")
        break
    if first_player[0] == 0 and second_player[0] == 9:
        first_player.append(first_player[0])
        first_player.append(second_player[0])
    elif first_player[0] == 9 and second_player[0] == 0:
        second_player.append(first_player[0])
        second_player.append(second_player[0])
    elif first_player[0] > second_player[0]:
        first_player.append(first_player[0])
        first_player.append(second_player[0])
    elif first_player[0] < second_player[0]:
        second_player.append(first_player[0])
        second_player.append(second_player[0])

    first_player.pop(0)
    second_player.pop(0)

if first_player:
    print(f'first {count_try}')
else:
    print(f'second {count_try}')
