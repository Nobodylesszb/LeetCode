#Given an n-ary tree, 
# return the postorder 
# traversal of its nodes' values.
#Recursion is easy to implement and understand by definition 
# https://en.wikipedia.org/wiki/Tree_traversal#Post-order_(LRN)
class Solution:
    def postorder(self,root):
        """
        :type:root :node
        :rtype:list[int]
        """
        res = []
        if root == None:
            return res 
        def recursion(root,res):
            for child in root.children:
                recursion(child,res)
            res.append(root.val)

        recursion(root,res)
        return res

    #iteration is basically pre order traversal but rather than go right 
    # first and then reverse its result

    def postorder1(self,root):
        res = []
        if root = None:
            return res
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)

            stack.extend(curr.children)
            return res[::-1]
  