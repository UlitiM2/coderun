nums = sorted(list(map(int, input().split())))
first_max = second_max = -float('inf')
first_min = second_min = float('inf')
for num in nums:
    if num > first_max:
        second_max, first_max = first_max, num
    elif num > second_max:
        second_max = num

    if num < first_min:
        second_min, first_min = first_min, num
    elif num < second_min:
        second_min = num

if first_max * second_max > first_min * second_min:
    print(second_max, first_max)
else:
    print(first_min, second_min)
