package com.bo.linkedList;

public class intersectionOfTwoLinkedList {
    
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null) return null;
    
        ListNode a = headA;
        ListNode b = headB;
        while(a!=b){
            a = a ==null ? headB:a.next;
            b = b == null? headA : b.next;   
        }
        return a;
    }
}

// It took me a while to understand why this worked, but I think I got it!

// It works because pointer A walks through List A and List B 
// (since once it hits null, it goes to List B's head).
// Pointer B also walks through List B and List A.
// Regardless of the length of the two lists, the sum of the lengths are 
// the same (i.e. a+b = b+a), 
// which means that the pointers sync up at the point of intersection.