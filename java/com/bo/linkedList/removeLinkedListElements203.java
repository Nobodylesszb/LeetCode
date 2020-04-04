package com.bo.linkedList;

public class removeLinkedListElements203 {
    public ListNode removeElements(ListNode head, int val) {
        if(head ==null){
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = dummy; 
        while(cur.next != null){
            if(cur.next.val == val){
                cur.next = cur.next.next;
            }else{
                cur = cur.next;
            }
        }
        return dummy.next;
    }

}