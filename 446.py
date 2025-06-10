def time_to_minutes(time_st):
    hh, mm = map(int, time_st.split(':'))
    return hh * 60 + mm


def minutes_to_time(minutes):
    total_count_days = minutes // (24 * 60)
    remaining_minutes = minutes % (24 * 60)
    hh = remaining_minutes // 60
    mm = remaining_minutes % 60
    return total_count_days, f"{hh:02d}:{mm:02d}"


def find_common_time(start1, start2, lap1, lap2):
    start1_min = time_to_minutes(start1)
    start2_min = time_to_minutes(start2)
    lap1_min = time_to_minutes(lap1)
    lap2_min = time_to_minutes(lap2)

    max_iterations = 1000
    for k in range(max_iterations):
        t_andrey = start1_min + k * lap1_min
        if (t_andrey - start2_min) >= 0 and (t_andrey - start2_min) % lap2_min == 0:
            return t_andrey
    return None


start_andrey = input().strip()
start_boris = input().strip()
lap_andrey = input().strip()
lap_boris = input().strip()


if start_andrey == start_boris:
    time_str = start_andrey
    print("Saturday")
    print(time_str)
elif start_andrey[3:] != start_boris[3:] and lap_andrey[3:] == lap_boris[3:]:
    print("Never")
else:
    t_meet = find_common_time(start_andrey, start_boris, lap_andrey, lap_boris)
    if t_meet is None:
        print("Never")
    else:
        total_days, time_str = minutes_to_time(t_meet)
        days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        day = total_days % 7
        print(days_of_week[day])
        print(time_str)
