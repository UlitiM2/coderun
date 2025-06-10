stack = []
cmd = input().strip()
i = 0
keys = {')': '(', '}': '{', ']': '['}
poss = True

for i in range(len(cmd)):
    if cmd[i] in '({[':
        stack.append(cmd[i])
    if cmd[i] in ')}]':
        if not stack:
            poss = False
            break
        if stack[-1] != keys[cmd[i]]:
            poss = False
            break
        stack.pop()

if stack:
    poss = False

print("yes" if poss else "no")
