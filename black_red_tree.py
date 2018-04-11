from enum import Enum


class BlackRedTree:

    NODE_TYPE = Enum('NODE_TYPE', 'BLACK RED')

    class TreeNode:

        def __init__(self, node_type):
            self.item = None

            self.node_type = node_type

    def __init__(self):
        print('Creating black-red tree!')

        self.root = BlackRedTree.TreeNode(BlackRedTree.NODE_TYPE.BLACK)


tree = BlackRedTree()

print(tree.root)
