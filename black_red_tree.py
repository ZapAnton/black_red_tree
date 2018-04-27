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

        if self.parent.parent.left_child == self.parent:
            return self.parent.parent.right_child
        else:
            return self.parent.parent.left_child

    def is_root(self) -> bool:
        return self.parent is None

    def __str__(self):
        return 'Node item: {:>5} Node color: {:>15} Node parent: {:>5}\
                Left child: {:>5} Right child: {:>5}'.format(
                    self.item,
                    self.node_type,
                    'No parent' if self.parent is None else self.parent.item,
                    'na' if self.left_child is None else self.left_child.item,
                    'na' if self.right_child is None else self.right_child.item
                )


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

    def __left_left_rotate(self, parent, grandparent):
        grandparent.left_child = parent.right_child

        if parent.right_child is not None:
            parent.right_child.parent = grandparent

        parent.parent = grandparent.parent

        if grandparent.parent.right_child == grandparent:
            grandparent.parent.right_child = parent
        elif grandparent.parent.left_child == grandparent:
            grandparent.parent.left_child = parent

        grandparent.parent = parent

        parent.right_child = grandparent

        (grandparent.node_type, parent.node_type) = \
            (parent.node_type, grandparent.node_type)

        if self.root == grandparent:
            self.root = parent

    def __left_right_rotate(self, new_node, parent, grandparent):
        parent.right_child = new_node.left_child

        if new_node.left_child is not None:
            new_node.left_child.parent = parent

        new_node.parent = grandparent

        if grandparent.left_child == parent:
            grandparent.left_child = new_node
        elif grandparent.right_child == parent:
            grandparent.right_child = new_node

        parent.parent = new_node

        new_node.left_child = parent

        if self.root == grandparent:
            self.root = new_node

        self.__left_left_rotate(new_node, grandparent)

    def __right_right_rotate(self, parent, grandparent):
        grandparent.right_child = parent.left_child

        parent.parent = grandparent.parent

        parent.left_child = grandparent

        grandparent.parent = parent

        (grandparent.node_type, parent.node_type) = \
            (parent.node_type, grandparent.node_type)

        if self.root == grandparent:
            self.root = parent

    def __right_left_rotate(self, new_node, parent, grandparent):
        parent.left_child = new_node.right_child

        new_node.parent = parent.parent

        new_node.right_child = parent

        parent.parent = new_node

        if self.root == grandparent:
            self.root = new_node

        self.__right_right_rotate(new_node, grandparent)

    def rebalance_tree(self, new_node: TreeNode):
        if new_node.is_root():
            new_node.node_type = NODE_TYPE.BLACK

            return

        parent = new_node.parent

        uncle = new_node.get_uncle_node()

        grandparent = new_node.parent.parent

        if grandparent is None:
            return

        if uncle is None or uncle.node_type == NODE_TYPE.BLACK:
            if (grandparent.left_child == parent) and \
               (parent.left_child == new_node):
                self.__left_left_rotate(parent, grandparent)
            elif (grandparent.left_child == parent) and \
                 (parent.right_child == new_node):
                self.__left_right_rotate(new_node, parent, grandparent)
            elif (grandparent.right_child == parent) and \
                 (parent.right_child == new_node):
                self.__right_right_rotate(parent, grandparent)
            elif (grandparent.right_child == parent) and \
                 (parent.left_child == new_node):
                self.__right_left_rotate(new_node, parent, grandparent)
        else:
            uncle.node_type = NODE_TYPE.BLACK

            parent.node_type = NODE_TYPE.BLACK

            grandparent.node_type = NODE_TYPE.RED

            self.rebalance_tree(grandparent)

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

    tree.insert(8)
    tree.insert(18)
    tree.insert(5)
    tree.insert(15)
    tree.insert(17)

    BlackRedTree.print_tree(tree.root)
