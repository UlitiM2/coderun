import math


def normalize(tr):
    a, b, c = sorted(tr)
    gcd_val = math.gcd(math.gcd(a, b), c)
    return a // gcd_val, b // gcd_val, c // gcd_val


n = int(input())
uniq_classes = set()

for _ in range(n):
    triangle = list(map(int, input().split()))
    normalized_triangle = normalize(triangle)
    uniq_classes.add(normalized_triangle)

print(len(uniq_classes))
