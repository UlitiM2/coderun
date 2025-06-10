n = int(input())
parent = {}
children = {}

for _ in range(n - 1):
    child, p = input().split()
    parent[child] = p
    if p not in children:
        children[p] = []
    children[p].append(child)

all_people = set(parent.keys()) | set(children.keys())
root = None
for person in all_people:
    if person not in parent:
        root = person
        break

height = {root: 0}
queue = [root]
while queue:
    current = queue.pop(0)
    if current in children:
        for child in children[current]:
            height[child] = height[current] + 1
            queue.append(child)

for name in sorted(height.keys()):
    print(name, height[name])

