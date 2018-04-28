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
