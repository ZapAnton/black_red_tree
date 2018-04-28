#[derive(Debug)]
enum NodeType {
    BLACK,
    RED,
}

#[derive(Debug)]
struct TreeNode<'a> {
    item: i32,

    node_type: NodeType,

    left_child: &'a Option<TreeNode<'a>>,

    right_child: &'a Option<TreeNode<'a>>,

    parent: &'a Option<TreeNode<'a>>,
}

impl<'a> TreeNode<'a> {
    fn new(item: i32) -> Self {
        TreeNode {
            item,
            node_type: NodeType::BLACK,
            left_child: &None,
            right_child: &None,
            parent: &None,
        }
    }
}

fn main() {
    let node1 = TreeNode::new(5);

    let node2 = TreeNode::new(5);

    println!("Created 2 nodes:\n1) {:?}\n2) {:?}", node1, node2);
}
