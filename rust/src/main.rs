mod tree_node;

use tree_node::TreeNode;

struct RedBlackTree {
    root: Option<*mut TreeNode>,
}

impl RedBlackTree {
    fn new() -> Self {
        RedBlackTree { root: None }
    }

    fn insert_node(root_node: Option<*mut TreeNode>, node: *mut TreeNode) -> Option<*mut TreeNode> {
        if root_node.is_none() {
            return Some(node);
        }

        unsafe {
            if (*node).item < (*root_node.unwrap()).item {
                (*root_node.unwrap()).left_child =
                    RedBlackTree::insert_node((*root_node.unwrap()).left_child, node);

                (*(*root_node.unwrap()).left_child.unwrap()).parent = root_node;
            } else if (*node).item > (*root_node.unwrap()).item {
                (*root_node.unwrap()).right_child =
                    RedBlackTree::insert_node((*root_node.unwrap()).right_child, node);

                (*(*root_node.unwrap()).right_child.unwrap()).parent = root_node;
            }
        }

        root_node
    }

    fn insert(&mut self, item: i32) {
        let new_node = Box::into_raw(Box::new(TreeNode::new(item)));

        self.root = RedBlackTree::insert_node(self.root, new_node);
    }
}

fn main() {
    let mut tree = RedBlackTree::new();

    tree.insert(5);

    tree.insert(1);

    tree.insert(6);

    unsafe {
        let root = &(*tree.root.unwrap());

        println!("{}", root);
    }
}
