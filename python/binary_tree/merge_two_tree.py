"""
If both trees are empty then we return empty.
Otherwise, we will return a tree. The root value will be t1.val + t2.val, except these values are 0 if the tree is empty.
The left child will be the merge of t1.left and t2.left, except these trees are empty if the parent is empty.
The right child is similar.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(5)
    print(len([root]))