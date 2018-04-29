#include <stdio.h>
#include <stdlib.h>

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


int main(int argc, char** argv) {
	TreeNode* node = new_node(5);

	TreeNode* parent = new_node(3);

	TreeNode* left_child = new_node(4);

	node->parent = parent;

	parent->right_child = node;

	node->left_child = left_child;

	left_child->parent = node;

	printf("Node: %d, Parent: %d, Left Child: %d\n",
			node->item, 
			node->parent->item, 
			node->left_child->item);

	free(left_child);

	free(node);

	free(parent);
}
