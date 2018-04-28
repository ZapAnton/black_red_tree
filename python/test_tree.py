import unittest
import random
from black_red_tree import BlackRedTree
from tree_node import NODE_TYPE


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


class MinMaxTest(unittest.TestCase):

    def test_min_max(self):
        tree = BlackRedTree()

        input_values = [random.randint(-1000, 1000) for _ in range(100)]

        for value in input_values:
            tree.insert(value)

        self.assertEqual(tree.min(), min(input_values))

        self.assertEqual(tree.max(), max(input_values))


class FindTest(unittest.TestCase):

    def test_find_values(self):
        tree = BlackRedTree()

        for value in range(10):
            tree.insert(value)

        self.assertEqual(tree.find(0).item, 0)

        self.assertEqual(tree.find(5).item, 5)

        self.assertIsNone(tree.find(10))


class ColorsTest(unittest.TestCase):

    def test_colors(self):
        tree = BlackRedTree()

        tree.insert(8)

        self.assertEqual(tree.find(8).node_type, NODE_TYPE.BLACK)

        tree.insert(18)

        self.assertEqual(tree.find(8).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(18).node_type, NODE_TYPE.RED)

        tree.insert(5)

        self.assertEqual(tree.find(8).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(18).node_type, NODE_TYPE.RED)

        self.assertEqual(tree.find(5).node_type, NODE_TYPE.RED)

        tree.insert(15)

        self.assertEqual(tree.find(8).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(18).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(5).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(15).node_type, NODE_TYPE.RED)

        tree.insert(17)

        self.assertEqual(tree.find(8).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(18).node_type, NODE_TYPE.RED)

        self.assertEqual(tree.find(5).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(15).node_type, NODE_TYPE.RED)

        self.assertEqual(tree.find(17).node_type, NODE_TYPE.BLACK)

        tree.insert(25)

        self.assertEqual(tree.find(8).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(18).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(5).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(15).node_type, NODE_TYPE.BLACK)

        self.assertEqual(tree.find(17).node_type, NODE_TYPE.RED)

        self.assertEqual(tree.find(25).node_type, NODE_TYPE.RED)


if __name__ == '__main__':
    unittest.main()
