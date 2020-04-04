
class Solution(object):
    # recursive
    def maxDepth(self,root):
        if not root:
            return 0
        if not root.children: return 1
        return max(self.maxDepth(node) for node in root.children) + 1

    # BFS (use a queue, the last level we see will be the depth)
    
    def maxDepth2(self,root):
        queue = []
        if root:
            queue.append((root,1))
        depth = 0
        for(node,level) in queue:
            depth = level
            queue +=[(child, level+1) for child in node.children]
        return depth
    

    # DFS (use a stack, use max to update depth)
    def maxDepth3(self,root):
        stack =[]
        if root: stack.append((root, 1))
        while stack:
            (node, d) = stack.pop()
            depth = max(depth, d)
            for child in node.children:
                stack.append((child, d+1))
        return depth



