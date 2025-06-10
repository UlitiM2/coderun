class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value, depth=1):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                return depth + 1
            else:
                return self.left.insert(value, depth + 1)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
                return depth + 1
            else:
                return self.right.insert(value, depth + 1)
        else:
            return None


numbers = list(map(int, input().split()))[:-1]

root = None
all_depths = []
for num in numbers:
    if root is None:
        root = TreeNode(num)
        all_depths.append(1)
    else:
        depth = root.insert(num)
        if depth is not None:
            all_depths.append(depth)

print(*all_depths)
