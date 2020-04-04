package com.bo.linkedList;

public class deleteNodeInLinkList237 {
    public void deleteNode(ListNode node){
        ListNode n = node.next;
        node.next = n.next;
        node.val = n.val;
    }

}