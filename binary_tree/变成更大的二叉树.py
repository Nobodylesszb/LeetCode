""""
We first traverse the tree "inorder" and keep track of all values. 
This will be all values in the tree in ascending order.
We then traverse the tree "reverse inorder" 
and set our node values as the suffix sums of values we have found.
"""

class Solution():
    def convertBst(self,root):
        def visit1(root):
            if root:
                visit1(root.left)
                vals.append(root.val)
                visit1(root.right)
        vals = []
        visit1(root)

        self.s = 0
        def visit2(root):
            if root:
                visit2(root.right)
                self.s += vals.pop()
                root.val = self.s
                visit2(root.left)
        visit2(root)

        return root

class Solution2:
    sum_values = 0
    
    def convertBST(self, root):
        if not root:
            return None
        self.convertBST(root.right)
        self.sum_values += root.val
        root.val = self.sum_values
        self.convertBST(root.left)
        return root
