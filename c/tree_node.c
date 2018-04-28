#include <stdio.h>

typedef struct TreeNode TreeNode;

struct TreeNode {
	int item;

	TreeNode* left_child;
	
	TreeNode* right_child;

	TreeNode* parent;
};

int main(int argc, char** argv) {
	puts("Hello from Node!");

	TreeNode node = {32};

	printf("Tree node: %d Parent: %p\n", node.item, node.parent);
}
