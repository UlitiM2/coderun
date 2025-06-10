from datetime import time

N = int(input())
data = [input().split() for _ in range(N)]
all_tills = []

for string in data:
    time_start = time(hour=int(string[0]), minute=int(string[1])).isoformat(timespec='minutes')
    time_end = time(hour=int(string[2]), minute=int(string[3])).isoformat(timespec='minutes')
    all_tills.append([time_start, time_end])

print(all_tills)
