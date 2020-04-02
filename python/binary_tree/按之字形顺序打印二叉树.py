class Btree(object):
    def __init__(self,value):
        self.left = None
        self.val = value
        self.right = None
        self.parent = None

    def insert_left(self,value):
        self.left = Btree(value)
        self.left.parent = self
        return self.left

    def insert_right(self,value):
        self.right = Btree(value)
        self.right.parent = self
        return self.right

    def show(self):
        print(self.val)

root = Btree('R')
a = root.insert_left('A')
b = root.insert_right('B')
c = a.insert_left('C')
d = a.insert_right('D')
e = b.insert_left('E')

class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result,nodes = [],[pRoot]
        right = True
        # 处理思路很好的，有一个二级机制，通过nextStack存下一节点的，这节点里面的值通过=nodes再转移到curStack里面
        # 但是在nextStack中可以调整顺序的
        while nodes:
            nextStack,curStack = [],[]
            if right:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            nextStack.reverse()
            right = not right
            result.append(curStack)
            nodes= nextStack
        return result

s =Solution()
print(s.Print(root))