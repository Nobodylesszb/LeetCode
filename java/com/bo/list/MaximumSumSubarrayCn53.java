package com.bo.list;

/**
 * @Auther: bo
 * @Date: 2020/4/2 17:03
 * @Version:
 * @Description:
 */
public class MaximumSumSubarrayCn53 {
    public int maxsubarray(int [] nums){
        int len = nums.length;
        int maxsum = Integer.MIN_VALUE;
        int sum = 0;
        for(int i =0;i<len;i++){
            sum=0;
            for(int j=i;j<len;j++){
                sum +=nums[j];
                maxsum = Math.max(maxsum,sum);
            }
        }
        return maxsum;

    }
}

