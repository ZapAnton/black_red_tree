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

    def __insert_item(self, item: int, node: TreeNode) -> TreeNode:
        if node is None:
            node = TreeNode(item, NODE_TYPE.RED)
        elif item < node.item:
            node.left_child = self.__insert_item(item, node.left_child)

            node.left_child.parent = node
        elif item > node.item:
            node.right_child = self.__insert_item(item, node.right_child)

            node.right_child.parent = node

        return node

    def insert(self, item: int):
        new_node = self.__insert_item(item, self.root)

        if self.root is None:
            self.root = new_node

            self.root.node_type = NODE_TYPE.BLACK

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
