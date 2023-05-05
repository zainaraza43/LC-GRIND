// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::cmp::max;
use std::rc::Rc;
fn d(root: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
    match root {
        Some(r) => {
            let (ld, lP) = d(r.borrow().left.clone());
            let (rd, rP) = d(r.borrow().right.clone());
            (max(ld, max(rd, lP + rP)), max(lP, rP) + 1)
        }
        None => (0, 0),
    }
}
impl Solution {
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let (d, _) = d(root);
        d
    }
}
