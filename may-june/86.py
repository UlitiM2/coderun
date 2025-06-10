import sys

bank_accounts = {}
sys.stdin = open('86.txt')
all_text = sys.stdin.readlines()

for j in all_text:
    text = j.split()
    if text[0] == 'DEPOSIT':
        if text[1] not in bank_accounts:
            bank_accounts[text[1]] = int(text[2])
        else:
            bank_accounts[text[1]] += int(text[2])
    elif text[0] == 'WITHDRAW':
        if text[1] not in bank_accounts:
            bank_accounts[text[1]] = -int(text[2])
        else:
            bank_accounts[text[1]] -= int(text[2])
    elif text[0] == 'BALANCE':
        if text[1] not in bank_accounts:
            print('ERROR')
        else:
            print(bank_accounts[text[1]])
    elif text[0] == 'TRANSFER':
        if text[1] not in bank_accounts:
            bank_accounts[text[1]] = -int(text[3])
        elif text[1] in bank_accounts:
            bank_accounts[text[1]] -= int(text[3])
        if text[2] not in bank_accounts:
            bank_accounts[text[2]] = int(text[3])
        elif text[2] in bank_accounts:
            bank_accounts[text[2]] += int(text[3])
    elif text[0] == 'INCOME':
        for i in bank_accounts:
            if bank_accounts[i] > 0:
                bank_accounts[i] = int((bank_accounts[i] * (100 + int(text[1])))/100)

