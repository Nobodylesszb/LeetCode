"""
Iterative:
设置一个Prev的参数方便之后的操作。

Step 1: 保存head reference
在While循环中，cur指针用来保留当前Head的位置，因为如果我们操作 head = head.next这一步并且没有对head的位置进行保留， 我们会失去对head的reference，导致我们之后不能进行反转操作。

Step 2: 保存head.next的reference
head的reference存好以后，我们还需要保存head.next的reference，原因是我们如果对第一个node进行了反转操作，node就指向我们之前定义好的prev上，而失去了对原先head.next这个位置的拥有权。

head.next这个reference，我们直接用head来保存即可，所以有了head = head.next这么一个操作。当然你要是想写的更加易懂，你也可以直接新创建一个函数，取名next，然后指向next = head.next。

Step 3: 反转
万事俱备，可以对cur指针进行反转了，指向之前定义的prev。

Step 4: Reference转移
最后不要忘记移动prev到cur的位置，不然prev的位置永远不变
"""

# class Solution:
#     def reverseList(self,head):
#         prev = None
#         while head:
#             cur = head
#             head = head.next
#             cur.next = prev
#             prev = cur 
#         return prev


# Recursive

class Solution:
    def reverseList1(self,head):
        if not head or not head.next:
            return head
        new_head = self.reverseList1(head.next) 
        next_node = head.next #  head -> next_node 
        next_node.next = head  #   head <- next_node 
        head.next = None      # [x] <- head <- next_node 
        return new_head

"""
Step 1: Base Case:
if not head or not head.next:
    return head
Base Case的返回条件是当head或者head.next为空，则开始返回


Step 2: Recurse到底
new_head = self.reverseList(head.next)
在做任何处理之前，我们需要不断的递归，直到触及到Base Case,。当我们移动到最后一个Node以后, 将这个Node定义为我们新的head, 取名new_head. 我们从new_head开始重复性的往前更改指针的方向


Step 3: 返回并且更改指针方向
next_node = head.next    #        head -> next_node 
next_node.next = head    #        head <- next_node 
head.next = None         # [x] <- head <- next_node 
"""