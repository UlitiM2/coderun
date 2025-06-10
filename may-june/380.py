n = int(input())
all_passengers = []
for _ in range(n):
    t, p = input().split()
    all_passengers.append([t, p])

all_passengers = sorted(all_passengers)
total_time = 1
uniq_row = {}
prev = all_passengers[0]
uniq_row[prev[1][:1]] = [prev[1][1:]]

for time, place in all_passengers[1:]:

    print(prev[1][:1], place[:1])

    if int(place[:1]) < int(prev[1][:1]):
        total_time += (int(time) - abs(int(prev[1][:1]) - int(place[:1])))
    elif int(place[:1]) == int(prev[1][:1]):
        total_time += 1
        total_time += int(time)
    else:
        if abs(int(prev[1][:1]) - int(place[:1])) == 1:
            total_time += (int(place[:1]) - abs(int(prev[1][:1]) - int(place[:1])))
            total_time += int(time)
        else:
            total_time += abs(int(prev[1][:1]) - int(place[:1]))
            total_time += int(time)

    prev = [time, place]

    if place[:1] not in uniq_row:
        uniq_row[place[:1]] = []
        uniq_row[place[:1]].append(place[1:])

    else:
        count_row_pass = 0
        for i in uniq_row[place[:1]]:
            if place[1:] in 'ABC' and i in 'ABC' and place[1:] < i:
                print('t', place[1:], i)
                count_row_pass += 1
            if place[1:] in 'DEF' and i in 'DEF' and place[1:] > i:
                print(place[1:], i)
                count_row_pass += 1
            print('tttt', total_time)
        if count_row_pass == 1:
            total_time += 5
        elif count_row_pass == 2:
            total_time += 15

        uniq_row[place[:1]].append(place[1:])


print(uniq_row)
print(total_time)
