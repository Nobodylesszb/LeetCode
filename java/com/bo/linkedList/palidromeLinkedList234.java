package com.bo.linkedList;

public class palidromeLinkedList234 {

    public ListNode root;
    
    public boolean isPalindrome(ListNode head){
         root = head;
        return(head ==null) ?true: _ispalindome(head);
    }
    public boolean _ispalindome(ListNode head){
        boolean flag = true;
        if(head.next !=null){
            flag = _ispalindome(head.next);
        }
        if(flag && root.val == head.val){
            root = root.next;
            return true;
        }
        return false;

    }

}