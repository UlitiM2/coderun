def change_phone(phone):
    p = ''
    for i in phone:
        if i in '0123456789':
            p += i
        else:
            continue
    return p


mass_of_phones = [change_phone(input()), change_phone(input()), change_phone(input()), change_phone(input())]
mass_to_check = []

for j in range(0, 4):
    curr_phone = mass_of_phones[j]
    if len(curr_phone) >= 11 and (curr_phone[0] == '7' or curr_phone[0] == '8'):
        code = curr_phone[1:4]
        number = curr_phone[4:11]
        mass_to_check.append((code, number))
    else:
        code = '495'
        number = curr_phone[-7:] if len(curr_phone) >= 7 else curr_phone.zfill(7)
        mass_to_check.append((code, number))

for p in range(1, 4):
    if mass_to_check[0] == mass_to_check[p]:
        print('YES')
    else:
        print('NO')
