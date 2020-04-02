#consider all the leaves of a binary tree.  
# From left to right order, the values of those leaves form a leaf value sequence
class Solution:
    def findleaf_inorder(self, root):  # LDR
        if root is None:
            return []
        elif (root.left is None) and (root.right is None):
            return [root.val]
        else:
            return self.findleaf_inorder(root.left) + self.findleaf_inorder(root.right)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.findleaf_inorder(root1) == self.findleaf_inorder(root2)