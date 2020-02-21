#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # find the mid nod
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse the second half
        node = None
        while slow:
            net = slow.next
            slow.next = node
            node = slow
            slow = net
        #compare the first and second half nodes
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
# @lc code=end

