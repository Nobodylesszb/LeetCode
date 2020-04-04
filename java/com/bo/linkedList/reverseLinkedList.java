package com.bo.linkedList;

public class reverseLinkedList {
    public ListNode reverselist(ListNode head){
        ListNode cur = head;
        ListNode prev = null;
        ListNode next = cur;
        
        while(cur !=null){
            if(cur.next ==null){
                cur.next = prev;
                break;
            }
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return cur;

    }

}