package com.bo.linkedList;

public class linkedListCycle141 {
    public boolean hasCycle(ListNode head) {
        if(head == null || head.next == null) return false;
        if(head.next == head) return true;
        ListNode nextnode = head.next;
        head.next = head;
        boolean iscycle = hasCycle(nextnode);
        return iscycle;
        
    }

}