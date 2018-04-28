#[derive(Debug)]
enum NodeType {
    BLACK,
    RED,
}

#[derive(Debug)]
struct TreeNode<'a> {
    item: i32,

    node_type: NodeType,

    left_child: Option<&'a TreeNode<'a>>,

    right_child: Option<&'a TreeNode<'a>>,

    parent: Option<&'a TreeNode<'a>>,
}

impl<'a> TreeNode<'a> {
    fn new(item: i32) -> Self {
        TreeNode {
            item,
            node_type: NodeType::RED,
            left_child: None,
            right_child: None,
            parent: None,
        }
    }

    fn is_root(&self) -> bool {
        self.parent.is_none()
    }
}

fn main() {
    let node1 = TreeNode::new(5);

    let node2 = TreeNode::new(5);

    println!("Created 2 nodes:\n1) {:?}\n2) {:?}", node1, node2);
}

#[cfg(test)]
mod test {

    use super::*;

    #[test]
    fn test_node_relations() {
        let mut parent = TreeNode::new(4);

        parent.node_type = NodeType::BLACK;

        let lc = TreeNode::new(6);

        let rc = TreeNode::new(7);

        let mut node = TreeNode::new(5);

        node.parent = Some(&parent);

        node.left_child = Some(&lc);

        node.right_child = Some(&rc);

        assert_eq!(node.item, 5);

        assert_eq!(node.parent.unwrap().item, 4);

        assert_eq!(node.left_child.unwrap().item, 6);

        assert_eq!(node.right_child.unwrap().item, 7);
    }

    #[test]
    fn test_is_root() {
        let parent = TreeNode::new(5);

        let mut node = TreeNode::new(4);

        node.parent = Some(&parent);

        assert!(!node.is_root());

        assert!(node.parent.unwrap().is_root());
    }
}
