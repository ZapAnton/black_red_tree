#include <stdlib.h>
#include "red_black_tree.h"

TreeNode* insert_node(TreeNode* new_node, TreeNode* root_node) {
	if (root_node == NULL) {
		return new_node;
	} else if (new_node->item < root_node->item) {
		root_node->left_child = insert_node(new_node, root_node->left_child);

		root_node->left_child->parent = root_node;
	} else if (new_node->item >= root_node->item) {
		root_node->right_child = insert_node(new_node, root_node->right_child);

		root_node->right_child->parent = root_node;
	}

	return root_node;
}

void insert(RedBlackTree* tree, int item) {
	TreeNode* new_node = construct_node(item);

	tree->root = insert_node(new_node, tree->root);
}

void print_tree(TreeNode* root_node) {
	if (root_node == NULL) {
		return;
	}

	print_tree(root_node->left_child);

	print_node(root_node);

	print_tree(root_node->right_child);
}
