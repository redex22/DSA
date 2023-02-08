class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, value):
        if self.key:
            if value < self.key:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            elif value > self.key:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)
        else:
            self.key = value

    def traverse_inorder(self):
        if self is None:
            return []
        return TreeNode.traverse_inorder(self.left) + [self.key] + TreeNode.traverse_inorder(self.right)

    def traverse_preorder(self):
        if self is None:
            return []
        return [self.key] + TreeNode.traverse_preorder(self.left) + TreeNode.traverse_preorder(self.right)

    def traverse_postorder(self):
        if self is None:
            return []
        return TreeNode.traverse_postorder(self.left) + TreeNode.traverse_postorder(self.right) + [self.key]

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def __len__(self):
        if self is None:
            return 0
        return 1 + TreeNode.__len__(self.left) + TreeNode.__len__(self.right)


if __name__ == "__main__":
    nodes_stack = [1, 3, 4, 6, 8, 7, 5]

    binary_tree = TreeNode(2)
    while nodes_stack:
        binary_tree.insert(nodes_stack.pop())

    print(binary_tree.traverse_inorder())    # [1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_tree.traverse_postorder())  # [1, 3, 4, 6, 8, 7, 5, 2]
    print(binary_tree.traverse_preorder())   # [2, 1, 5, 4, 3, 7, 6, 8]
    print(binary_tree.height())              # 4 (we have to move 4 positions to get the deepest leave
    print(len(binary_tree))                  # 8 (we have eight elements)
