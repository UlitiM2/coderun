a = int(input())
b = int(input())
c = int(input())

numerator = 3 * a + b - c
if numerator <= 0:
    i = 0
else:
    i = (numerator + 2) // 3

print(i)
