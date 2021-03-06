#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "tree_node.h"

void test_free_node() {
	printf("Testing free_node function: ");

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

	free_node(&parent);

	printf("\x1b[32mOk!\x1b[0m\n");
}

void test_relations() {
	printf("Testing node relations function: ");

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

	printf("\x1b[32mOk!\x1b[0m\n");
}

void test_get_uncle() {
	printf("Testing get_uncle function: ");

	TreeNode* node = new_node(5);

	TreeNode* parent = new_node(3);

	TreeNode* grandparent = new_node(2);

	TreeNode* uncle = new_node(1);

	assert(get_uncle(node) == NULL);

	node->parent = parent;

	parent->right_child = node;

	assert(get_uncle(node) == NULL);

	parent->parent = grandparent;

	grandparent->right_child = parent;

	assert(get_uncle(node) == NULL);

	grandparent->left_child = uncle;

	assert(get_uncle(node) == uncle);

	free_node(&grandparent);

	printf("\x1b[32mOk!\x1b[0m\n");
}

void test_print_node() {
	TreeNode* node = new_node(5);

	TreeNode* parent = new_node(2);

	TreeNode* right_child = new_node(6);

	parent->right_child = node;

	node->parent = parent;

	node->right_child = right_child;

	right_child->parent = node;

	puts("Testing print_node function:\n");

	print_node(node);

	puts("");

	print_node(parent);

	puts("");

	print_node(right_child);

	free_node(&parent);
}


int main(int argc, char** argv) {
	test_relations();

	test_free_node();

	test_get_uncle();

	test_print_node();

	return 0;
}
