from enum import Enum


NODE_TYPE = Enum('NODE_TYPE', 'BLACK RED')


class TreeNode:

    def __init__(self, node_type):
        self.item = None

        self.node_type = node_type

        self.left_child = TreeNode(NODE_TYPE.BLACK)

        self.right_child = TreeNode(NODE_TYPE.BLACK)


class BlackRedTree:

    def __init__(self):
        print('Creating black-red tree!')

        self.root = TreeNode(NODE_TYPE.BLACK)


tree = BlackRedTree()

print(tree.root)
