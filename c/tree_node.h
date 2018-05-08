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

TreeNode* new_node(int item);

void free_node(TreeNode** node);
