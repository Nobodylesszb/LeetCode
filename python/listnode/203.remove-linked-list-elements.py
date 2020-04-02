"""
关键点解析
链表的基本操作（删除指定节点）
虚拟节点dummy 简化操作
其实设置dummy节点就是为了处理特殊位置（头节点），这这道题就是如果头节点是给定的需要删除的节点呢？ 为了保证代码逻辑的一致性，即不需要为头节点特殊定制逻辑，才采用的虚拟节点。

如果连续两个节点都是要删除的节点，这个情况容易被忽略。 eg:
// 只有下个节点不是要删除的节点才更新current
if (!next || next.val !== val) {
    current =  next;
}
"""
"""
Before writing any code, it's good to make a list of edge cases that we need to consider. This is so that we can be certain that we're not overlooking anything while coming up with our algorithm, and that we're testing all special cases when we're ready to test. These are the edge cases that I came up with.

The linked list is empty, i.e. the head node is None.
Multiple nodes with the target value in a row.
The head node has the target value.
The head node, and any number of nodes immediately after it have the target value.
All of the nodes have the target value.
The last node has the target value.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self,head,val):
        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy_head.next


        def removeElements1(self,head:ListNode,val:int)->ListNode:
            prev = ListNode(0)
            prev.next = head
            cur = prev
            while cur.next:
                if cur.next.val == val:
                    cur.next == cur.next.next
                else:
                    cur = cur.next
            return prev.next


