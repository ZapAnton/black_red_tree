#include "tree_node.h"

typedef struct RedBlackTree RedBlackTree;
struct RedBlackTree {
	TreeNode* root;
};

void insert(RedBlackTree* tree, int item);

void print_tree(TreeNode* tree);

TreeNode* insert_node(TreeNode* new_node, TreeNode* root_node);
