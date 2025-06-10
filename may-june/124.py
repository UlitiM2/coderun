class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)


def find_leaves(node, leaves):
    if node is None:
        return
    if node.left is None and node.right is None:
        leaves.append(node.value)
    find_leaves(node.left, leaves)
    find_leaves(node.right, leaves)


numbers = list(map(int, input().split()))[:-1]

root = None
for num in numbers:
    if root is None:
        root = TreeNode(num)
    else:
        root.insert(num)

leaves = []
if root:
    find_leaves(root, leaves)

leaves.sort()
print('\n'.join(map(str, leaves)))
