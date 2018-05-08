#include <stdio.h>
#include <stdlib.h>
#include "tree_node.h"

TreeNode* new_node(int item) {
	TreeNode* node = malloc(sizeof(TreeNode));

	node->item = item;

	node->node_type = RED;

	node->right_child = NULL;

	node->left_child = NULL;

	node->parent = NULL;

	return node;
}

void free_node(TreeNode** node) {
	if (*node == NULL) {
		return;
	}

	if ((*node)->parent != NULL) {
		(*node)->parent = NULL;
	}

	free_node(&(*node)->left_child);

	free_node(&(*node)->right_child);

	free(*node);

	*node = NULL;
}
