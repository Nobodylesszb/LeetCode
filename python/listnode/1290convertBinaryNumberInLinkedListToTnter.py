class  Solution(object):
    def getdecimalvalue(self,head):
        ans =0
        while head:
            ans = (ans<<1)|head.val
            head = head.next
        return ans