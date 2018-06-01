#include <stdlib.h>
#include "red_black_tree.h"

TreeNode* insert_node(TreeNode* new_node, TreeNode* root_node) {
	return NULL;
}

void insert(RedBlackTree* tree, int item) {
	TreeNode* new_node = construct_node(item);

	tree->root = insert_node(new_node, tree->root);
}
