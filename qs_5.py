mass = []
while True:
    i = int(input())
    if i == -2000000000:
        break
    mass.append(i)

flag_const = True
flag_ascending = True
flag_descending = True

for j in range(len(mass)-1):
    if mass[j] != mass[j+1]:
        flag_const = False
    if mass[j] >= mass[j+1]:
        flag_ascending = False
    if mass[j] <= mass[j+1]:
        flag_descending = False

if flag_const:
    print("CONSTANT")
elif flag_ascending:
    print("ASCENDING")
elif flag_descending:
    print("DESCENDING")
else:
    flag_weak_ascending = all(mass[j] <= mass[j+1] for j in range(len(mass)-1))
    flag_weak_descending = all(mass[j] >= mass[j+1] for j in range(len(mass)-1))
    if flag_weak_ascending:
        print("WEAKLY ASCENDING")
    elif flag_weak_descending:
        print("WEAKLY DESCENDING")
    else:
        print("RANDOM")
