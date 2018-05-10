#[derive(Debug)]
enum NodeType {
    BLACK,
    RED,
}

#[derive(Debug)]
struct TreeNode {
    item: i32,

    node_type: NodeType,

    left_child: Option<*const TreeNode>,

    right_child: Option<*const TreeNode>,

    parent: Option<*const TreeNode>,
}

impl TreeNode {
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

    fn get_uncle(&self) -> Option<*const TreeNode> {
        if self.is_root() {
            return None;
        }

        unsafe {
            let parent = self.parent;

            if let Some(grandparent) = (*parent.unwrap()).parent {
                if (*grandparent).left_child == parent {
                    (*grandparent).right_child
                } else {
                    (*grandparent).left_child
                }
            } else {
                None
            }
        }
    }
}

fn main() {}

#[cfg(test)]
mod test {

    use super::*;

    /*#[test]
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
    }*/

    #[test]
    fn test_is_root() {
        let parent = TreeNode::new(5);

        let mut node = TreeNode::new(4);

        node.parent = Some(&parent as *const TreeNode);

        assert!(!node.is_root());

        unsafe {
            assert!((*node.parent.unwrap()).is_root());
        }
    }

    #[test]
    fn test_uncle() {
        let mut grandparent = TreeNode::new(10);

        let mut parent = TreeNode::new(15);

        let mut uncle = TreeNode::new(8);

        let mut node = TreeNode::new(18);

        assert!(node.get_uncle().is_none());

        node.parent = Some(&parent as *const TreeNode);

        parent.right_child = Some(&node as *const TreeNode);

        assert!(node.get_uncle().is_none());

        parent.parent = Some(&grandparent as *const TreeNode);

        grandparent.right_child = Some(&parent as *const TreeNode);

        assert!(node.get_uncle().is_none());

        grandparent.left_child = Some(&uncle as *const TreeNode);

        uncle.parent = Some(&grandparent as *const TreeNode);

        assert!(node.get_uncle().is_some());
    }
}
