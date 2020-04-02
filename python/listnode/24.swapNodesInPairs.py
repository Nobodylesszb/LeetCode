# 题目描述
# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

"""
思路
设置一个dummy 节点简化操作,dummy next 指向head。

初始化first为第一个节点
初始化second为第二个节点
初始化current为dummy
first.next = second.next
second.next = first
current.next = second
current 移动两格
重复
"""

"""
Here, pre is the previous node. Since the head doesn't have a previous node, I just use self instead. Again, a is the current node and b is the next node.

To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references. Instead of thinking about in what order I change them, I just change all three at once
"""
class Solution:
    def swapPairs(self,head):
        pre, pre.next = self, head
        while pre.next  and pre.next.next:
            a = pre.next
            b = a.next
            pre.next,b.next,a.next = b ,a ,b.next
            pre = a
        return self.next


