rules = {}
all_sides = ['N', 'S', 'W', 'E', 'U', 'D']
for i in all_sides:
    curr_str = input()
    rules[i] = curr_str

side, number = input().split()


def count_moves(command, M):
    dp = {cmd: {} for cmd in rules}

    for cmd in rules:
        dp[cmd][1] = 1

    for m in range(2, M + 1):
        for cmd in rules:
            total = 1
            for sub_cmd in rules[cmd]:
                total += dp[sub_cmd][m - 1]
            dp[cmd][m] = total
    return dp[command][M]


print(count_moves(side, int(number)))
