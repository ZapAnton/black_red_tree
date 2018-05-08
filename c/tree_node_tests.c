#include <assert.h>
#include <stdlib.h>
#include "tree_node.h"

void test_free_node() {
	TreeNode* parent = new_node(3);

	TreeNode* left_child = new_node(4);

	TreeNode* node = new_node(5);

	free_node(&node);

	assert(node == NULL);

	node = new_node(8);

	parent->right_child = node;

	node->parent = parent;

	node->left_child = left_child;

	left_child->parent = node;

	free_node(&parent->right_child);

	assert(parent->right_child == NULL);
}

void test_relations() {
	TreeNode* node = new_node(5);

	TreeNode* parent = new_node(3);

	TreeNode* left_child = new_node(4);

	node->parent = parent;

	parent->right_child = node;

	node->left_child = left_child;

	left_child->parent = node;

	assert(node->item == 5);

	assert(node->parent->item == 3);

	assert(node->left_child->item == 4);

	assert(node->right_child == NULL);

	free_node(&node);
}


int main(int argc, char** argv) {
	test_relations();

	test_free_node();

	return 0;
}
