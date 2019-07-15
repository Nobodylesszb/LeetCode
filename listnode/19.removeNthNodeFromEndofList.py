"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5. Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

"""
双指针，指针A先移动n次， 指针B再开始移动。当A到达null的时候， 指针b的位置正好是倒数n

我们可以设想假设设定了双指针p和q的话，当q指向末尾的NULL，p与q之间相隔的元素个数为n时，那么删除掉p的下一个指针就完成了要求。

设置虚拟节点dummyHead指向head

设定双指针p和q，初始都指向虚拟节点dummyHead

移动q，直到p与q之间相隔的元素个数为n

同时移动p与q，直到q指向的为NULL

将p的下一个节点指向下下个节点
"""
"""
关键点
链表这种数据结构的特点和使用

使用双指针

使用一个dummyHead简化操作
"""

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        