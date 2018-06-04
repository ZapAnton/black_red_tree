#include <stdio.h>
#include <stdlib.h>
#include "tree_node.h"

TreeNode* construct_node(int item) {
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

TreeNode* get_uncle(TreeNode* node) {
	if (is_root(node)) {
		return NULL;
	}

	TreeNode* parent = node->parent;

	if (is_root(parent)) {
		return NULL;
	}

	TreeNode* grandparent = parent->parent;

	if (grandparent->right_child == parent) {
		return grandparent->left_child;
	} else {
		return grandparent->right_child;
	}
}

int is_root(TreeNode* node) {
	if (node != NULL) {
		return node->parent == NULL;
	} else {
		return 0;
	}
}

void print_node(TreeNode* node) {
	if (node == NULL) {
		return;
	}

	char parent_item_buff[12];
	
	char left_item_buff[12];

	char right_item_buff[12];
	
	if (is_root(node)) {
		sprintf(parent_item_buff, "%s", "NULL");
	} else {
		sprintf(parent_item_buff, "%d", node->parent->item);
	}

	if (node->left_child == NULL) {
		sprintf(left_item_buff, "%s", "NULL");
	} else {
		sprintf(left_item_buff, "%d", node->left_child->item);
	}

	if (node->right_child == NULL) {
		sprintf(right_item_buff, "%s", "NULL");
	} else {
		sprintf(right_item_buff, "%d", node->right_child->item);
	}

	printf("Node: %d, Color: %s, Parent: %s, Left child: %s, Right child: %s\n",
			node->item,
			node->node_type == BLACK ? "BLACK" : "RED",
			parent_item_buff,
			left_item_buff,
			right_item_buff);
}
