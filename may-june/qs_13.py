def make_symmetric(sequence):
    n = len(sequence)
    for i in range(n):
        if sequence[i:] == sequence[i:][::-1]:
            return sequence[:i][::-1]
    return []


N = int(input())
mass = input().split()

result = make_symmetric(mass)
if len(result) != 0:
    print(len(result))
    print(' '.join(result))
else:
    print('0')
