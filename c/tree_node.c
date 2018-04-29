#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef enum{
	BLACK,
	RED,
} NodeType;

typedef struct TreeNode TreeNode;
struct TreeNode {
	int item;

	NodeType node_type;

	TreeNode* left_child;
	
	TreeNode* right_child;

	TreeNode* parent;
};

TreeNode* new_node(int item) {
	TreeNode* node = malloc(sizeof(TreeNode));

	node->item = item;

	node->node_type = RED;

	node->right_child = NULL;

	node->left_child = NULL;

	return node;
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

	free(left_child);

	free(node);

	free(parent);
}


int main(int argc, char** argv) {
	test_relations();
}
