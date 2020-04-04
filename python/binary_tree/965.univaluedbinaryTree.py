import collections
class Solution(object):
    
    # using the queue
    def isUnivalTree(self,root):
        dq = collections.deque([root])
        while dq:
            node = dq.popleft()
            if node.val != root.val:
                return False
            dq.extend([n for n in (node.left, node.right) if n])
        return True