package com.bo.string;

public class ValidPalindrome125 {
    public static boolean ispalindrome(String str){
        if(str.isEmpty()){
            return true;
        }
        int left = 0,right = str.length()-1;
        char head,tail;
        while(left<=right){
            head = str.charAt(left);
            tail = str.charAt(right);
            if(!Character.isLetterOrDigit(head)){
                left++;
            }else if(!Character.isLetterOrDigit(tail)){
                tail--;
            }else{
                if(Character.toLowerCase(head) !=Character.toLowerCase(tail)){
                    return false;
                }
                head++;
                tail--;
            }
        }
        return true;
    }

    public static void main(String[] args){  
        String a = "afsadadsg";
        System.out.println(ispalindrome(a));
    }

}