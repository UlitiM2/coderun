A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

min_side_1, min_side_2 = sorted([A, B, C])[0], sorted([A, B, C])[1]
if (min_side_1 <= D and min_side_2 <= E) or (min_side_2 <= D and min_side_1 <= E):
    print("YES")
else:
    print("NO")
