mass_nums = list(map(int, input().split()))
mass_nums = sorted(mass_nums, reverse=True)
multiplication_1 = mass_nums[0] * mass_nums[1] * mass_nums[2]
multiplication_2 = mass_nums[0] * mass_nums[-1] * mass_nums[-2]
if multiplication_1 > multiplication_2:
    print(*mass_nums[0:3])
else:
    print(mass_nums[0], mass_nums[-1], mass_nums[-2])

