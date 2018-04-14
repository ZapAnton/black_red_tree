from enum import Enum


NODE_TYPE = Enum('NODE_TYPE', 'BLACK RED')


class TreeNode:

    def __init__(self, item: int, node_type: NODE_TYPE):
        self.item = item

        self.node_type = node_type

        self.left_child = None

        self.right_child = None

        self.parent = None

    def get_uncle_node(self):
        if self.parent is None:
            return None

        if self.parent.parent is None:
            return None

        return self.parent.parent.right_child

    def is_root(self) -> bool:
        return self.parent is None

    def __str__(self):
        return 'Node item: {:>5} Node color: {:>15} Node parent: {:>5}'.format(
                      self.item,
                      self.node_type,
                      'No parent' if self.parent is None else self.parent.item)


class BlackRedTree:

    def __init__(self):
        print('Creating black-red tree!')

        self.root = None

    def __insert_item(self, new_node: TreeNode, root: TreeNode) -> TreeNode:
        if root is None:
            return new_node
        elif new_node.item < root.item:
            root.left_child = self.__insert_item(new_node, root.left_child)

            root.left_child.parent = root
        elif new_node.item > root.item:
            root.right_child = self.__insert_item(new_node, root.right_child)

            root.right_child.parent = root

        return root

    def rebalance_tree(self, new_node: TreeNode):
        if new_node.is_root():
            new_node.node_type = NODE_TYPE.BLACK

            return

        elif new_node.parent.node_type == NODE_TYPE.BLACK:

            return

        new_node_uncle = new_node.get_uncle_node()

        new_node_grandparent = new_node.parent.parent

        if new_node_uncle is None:
            return

        if new_node_uncle.node_type == NODE_TYPE.RED:
            new_node_uncle.node_type = NODE_TYPE.BLACK

            new_node.parent.node_type = NODE_TYPE.BLACK

            new_node_grandparent.node_type = NODE_TYPE.RED

            self.rebalance_tree(new_node_grandparent)

    def insert(self, item: int):
        new_node = TreeNode(item, NODE_TYPE.RED)

        self.root = self.__insert_item(new_node, self.root)

        self.rebalance_tree(new_node)

    def print_tree(node: TreeNode):
        if node is not None:
            BlackRedTree.print_tree(node.left_child)

            print(node)

            BlackRedTree.print_tree(node.right_child)


if __name__ == '__main__':
    tree = BlackRedTree()

    tree.insert(50)

    tree.insert(30)

    tree.insert(20)

    tree.insert(40)

    tree.insert(70)

    tree.insert(60)

    tree.insert(80)

    BlackRedTree.print_tree(tree.root)
