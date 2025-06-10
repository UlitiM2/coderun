def format_num(num):
    return f'.{num}' if num < 10 else str(num)


n, weekday = input().split()
week_days = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday']
idx = week_days.index(weekday)
nums = [i for i in range(1, int(n)+1)]
point_end = (7-idx)
print('.. ' * idx, end='')
print(*[format_num(num) for num in nums[:7-idx]])
point_s = point_end
while point_end < int(n) + 1:
    point_end += 7
    print(*[format_num(num) for num in nums[point_s:point_end]])
    point_s += 7
