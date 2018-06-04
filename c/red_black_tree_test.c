#include <stdio.h>
#include "red_black_tree.h"

int main(int argc, char** argv) {
	RedBlackTree tree;

	tree.root = NULL;

	insert(&tree, 5);
	insert(&tree, 1);
	insert(&tree, 3);
	insert(&tree, 8);
}
