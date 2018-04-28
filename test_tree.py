import unittest
import random
from black_red_tree import BlackRedTree


class TestInsert(unittest.TestCase):

    def test_inorder(self):
        list_size = 20

        tree = BlackRedTree()

        input_values = list(range(list_size))

        random.shuffle(input_values)

        for value in input_values:
            tree.insert(value)

        for i, item in enumerate(tree.inorder_items()):
            self.assertEqual(i, item)


if __name__ == '__main__':
    unittest.main()
