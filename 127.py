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


def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


def check_AVL(node):
    if node is None:
        return True
    len_of_1 = height(node.left)
    len_of_2 = height(node.right)
    if abs(len_of_1 - len_of_2) > 1:
        return False
    return check_AVL(node.left) and check_AVL(node.right)


numbers = list(map(int, input().split()))[:-1]

root = None
for num in numbers:
    if root is None:
        root = TreeNode(num)
    else:
        root.insert(num)

print("YES" if check_AVL(root) else "NO")
