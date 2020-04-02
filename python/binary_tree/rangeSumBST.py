class Solution:
    def rangeSumBST(self, root, L, R):
        return self.inorder(root, 0, L, R)

    def inorder(self,root, value, L, R):
        if root:
            value = self.inorder(root.left, value, L, R)
            if root.val >= L and root.val <= R:
                value += root.val
            value = self.inorder(root.right, value, L, R)

        return value