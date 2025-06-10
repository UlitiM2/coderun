n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    total_sum = 2
    a, b = 1, 1
    for _ in range(3, n+1):
        c = a+b
        total_sum += c
        a, b = b, c
    print(total_sum)
