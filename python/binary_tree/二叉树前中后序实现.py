# 首先我们创建一个二叉树结点类。并加入插入节点的方法

class Btree(object):
    def __init__(self,value):
        self.left = None
        self.data = value
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
        print(self.data)

# 手动创建一个二叉树 root为根节点，a,b分别为root的左右子节点，c、d分别为a的左右子节点，e是b的左子节点

# root = Btree('R')
# a = root.insert_left('A')
# b = root.insert_right('B')
# c = a.insert_left('C')
# d = a.insert_right('D')
# e = b.insert_left('E')


"""
二叉树中最常见的就是它的三种遍历方式：前序遍历、中序遍历、后序遍历。
前序遍历的方式为：中-左-右；中序遍历的方式为：左-中-右；
后序遍历的方式为：左-右-中。需要注意的是：对于一棵排序二叉树，它的中序遍历就是各元素从小到大的排序。
使用递归的方式来对二叉树进行三种遍历，三个函数的思路完全一样，十分简单。
"""

class OrderMethod():
    def pre_order(self,node):
        if node.data:
            node.show()
            if node.left:
                self.pre_order(node.left)
            if node.right:
                self.pre_order(node.right)

    def middle_order(self,node):
        if node.data: 
            if node.left:
                self.middle_order(node.left)
            node.show()
            if node.right:
                self.middle_order(node.right)

    def post_order(self,node):
        if node.data:
            if node.left:
                self.post_order(node.left)
            if node.right:
                self.post_order(node.right)
            node.show()

    def lookup(self,root):
        stack = [root]
        while stack:
            current = stack.pop(0)
            current.show()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

    def insert(self,node,value):
        if value>node.data:
            if node.right == None:
                node.insert_right(value)
            else:
                self.insert(node.right,value)
        else:
            if node.left == None:
                node.insert_left(value)
            else:
                self.insert(node.left,value)

    def search(self,node,k):
        while node != None:
            if k < node.data:
                node = node.left
            elif k >node.data:
                node = node.right
            else:
                return k
        return 0 




root = Btree('R')
a = root.insert_left('A')
b = root.insert_right('B')
c = a.insert_left('C')
d = a.insert_right('D')
e = b.insert_left('E')
f = b.insert_right('F')

M = OrderMethod()

print(M.pre_order(root))
"""
output:
R
A
C
D
B
E
None
"""

# print(M.middle_order(root))

"""
output:
C
A
D
R
E
B
None
"""
# print(M.post_order(root))

"""
C
D
A
E
B
R
None

"""
# print(M.lookup(root))
"""
output
R
A
B
C
D
E
None
"""

# L = [4,3,6,13,61,38,22,41]
# new_Root= Btree(L[0])        # 创建根节点
# for i in range(1,len(L)):
#     M.insert(new_Root,L[i])
# print(M.middle_order(new_Root))

"""
output:
3
4
6
13
22
38
41
61
None
"""


