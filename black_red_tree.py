from enum import Enum


NODE_TYPE = Enum('NODE_TYPE', 'BLACK RED')


class TreeNode:

    def __init__(self, item: int, node_type: NODE_TYPE):
        self.item = item

        self.node_type = node_type

        self.left_child = TreeNode(NODE_TYPE.BLACK)

        self.right_child = TreeNode(NODE_TYPE.BLACK)


class BlackRedTree:

    def __init__(self):
        print('Creating black-red tree!')

        self.root = TreeNode(NODE_TYPE.BLACK)


tree = BlackRedTree()

print(tree.root)
