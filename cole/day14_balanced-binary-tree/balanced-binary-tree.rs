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
use std::rc::Rc;
use std::cell::RefCell;

trait BalancedTree {
    fn walk(&mut self) -> i32;
    fn balanced(&mut self) -> bool;
}

impl BalancedTree for TreeNode {

    fn walk(&mut self) -> i32 {
        let l = self.left.as_mut().map(|node| node.borrow_mut().walk()).unwrap_or(0);
        let r = self.right.as_mut().map(|node| node.borrow_mut().walk()).unwrap_or(0);
        match (l - r).abs() > 1  || l < 0 || r < 0 {
            true => -1,
            false => 1 + i32::max(l, r)
        }
    }
    fn balanced(&mut self) -> bool {
        self.walk() > 0
    }
}

impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        root.map(|node| node.borrow_mut().balanced()).unwrap_or(true)
    }
}