# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

#递归
import math
class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        if(not root.left and not root.right):
            return 1
        return  1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#使用迭代
# 关键点解析
# 队列

# 队列中用 Null(一个特殊元素)来划分每层，或者在对每层进行迭代之前保存当前队列元素的个数（即当前层所含元素个数）

# 树的基本操作- 遍历 - 层次遍历（BFS）

class Solution1:
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
            level =queue
        return depth