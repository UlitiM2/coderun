from math import sqrt
a, b, c = list(map(int, input().split()))
discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x_1 = (- b - sqrt(discriminant)) / (2 * a)
    x_2 = (- b + sqrt(discriminant)) / (2 * a)
    print("2")
    print(round(x_1, 6), round(x_2, 6))
elif discriminant == 0:
    x = (- b) / (2 * a)
    print("1")
    print(round(x, 6))
else:
    print("0")

