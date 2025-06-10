curr_temp, wanted_temp = map(int, input().split())
mode = input()

if mode == 'fan':
    print(curr_temp)
elif mode == 'auto':
    print(wanted_temp)
elif mode == 'heat':
    if curr_temp <= wanted_temp:
        print(wanted_temp)
    else:
        print(curr_temp)
elif mode == 'freeze':
    if curr_temp >= wanted_temp:
        print(wanted_temp)
    else:
        print(curr_temp)

