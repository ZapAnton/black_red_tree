from enum import Enum


NODE_TYPE = Enum('NODE_TYPE', 'BLACK RED')


class TreeNode:

    def __init__(self, item: int, node_type: NODE_TYPE):
        self.item = item

        self.node_type = node_type

        self.left_child = None

        self.right_child = None


class BlackRedTree:

    def __init__(self):
        print('Creating black-red tree!')

        self.root = None

    def __insert_item(self, item: int, node: TreeNode) -> TreeNode:
        if node is None:
            node = TreeNode(item, NODE_TYPE.RED)
        elif item < node.item:
            node.left_child = self.__insert_item(item, node.left_child)
        elif item > node.item:
            node.right_child = self.__insert_item(item, node.right_child)

        return node

    def insert(self, item: int):
        new_node = self.__insert_item(item, self.root)

        if self.root is None:
            self.root = new_node

            self.root.node_type = NODE_TYPE.BLACK

            return

    def print_tree(node: TreeNode):
        if node is not None:
            BlackRedTree.print_tree(node.left_child)

            print(node.item, '----', node.node_type)

            BlackRedTree.print_tree(node.right_child)


if __name__ == '__main__':
    tree = BlackRedTree()

    BlackRedTree.print_tree(tree.root)

    tree.insert(50)

    tree.insert(30)

    tree.insert(20)

    tree.insert(40)

    tree.insert(70)

    tree.insert(60)

    tree.insert(80)

    BlackRedTree.print_tree(tree.root)
