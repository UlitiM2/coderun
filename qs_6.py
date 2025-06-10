numbers = input().split()
a = int(numbers[0])
b = int(numbers[1])


def compute_nod(x, y):
    while y:
        x, y = y, x % y
    return x


nod = compute_nod(a, b)
nok = (a * b) // nod
print(nod, nok)
