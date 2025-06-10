N = int(input())
mass = list(map(int, input().split()))
current = 1
stack_tupik = []
possible = True

for i in mass:
    stack_tupik.append(i)
    while stack_tupik and stack_tupik[-1] == current:
        stack_tupik.pop()
        current += 1

if stack_tupik:
    possible = False

print("YES" if possible else "NO")
