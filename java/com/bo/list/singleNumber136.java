package com.bo.list;

public class singleNumber136 {
    public static int singleNumber(int[] nums){
        int ans =0;
        for (int i = 0; i < nums.length; i++) {
            ans ^= nums[i];
        }
        return ans;
    }   
    public static void main(String[] args){
        int[] b = {2,4,2,5,5};
        int ans;
        ans = singleNumber(b);
        System.out.println(ans);
    }
}