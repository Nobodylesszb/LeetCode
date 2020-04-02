#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if (not root.left and not root.right):
            return 1

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
# @lc code=end

class SolutionBfs:
    def maxDepth(self,root):
        depth = 0
        level = [root] if root else []
        while level:
            depth +=1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
        return depth

    def maxDepth2(self,root):
        if root is None:
            return 0

        queue = [root]
        depth = 0
        while queue:
            depth +=1
            for i in range(len(queue)):
                cur_root = queue.pop(0)
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth

class SolutionDfs:
    def maxDepth(self,root):
        depth = 0
        stack = [(root,1)]
        while stack:
            root.leng = stack.pop()
            if not root:
                return 0
            if leng > depth:
                depth = leng
            
            if root.right:
                stack.append((root.right,leng+1))
            if root.left:
                stack.append((root.left,leng+1))
    return depth


