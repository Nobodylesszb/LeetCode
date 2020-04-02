package com.bo.list;

/**
 * @Auther: bo
 * @Date: 2020/4/2 13:44
 * @Version:
 * @Description:
 */
public class RemoveDuplicatesfromSortedArray26 {
    public static int removeDuplicates(int [] A){
        if(A ==null || A.length ==0){
            return 0;
        }
        int index =0;
        for(int i =1;i<A.length;i++){
            if(A[index] == A[i]){
                continue;
            }else {
                A[++index] = A[i];
            }
        }
        return index +1;
    }

    public static void main(String[] args) {
        int [] arr = {1,1,2,2,5,5,6,7};
        int i = removeDuplicates(arr);
        System.out.println(i);
    }
}


// python two point method
//class Solution:
//        def removeDuplicates(self, nums: List[int]) -> int:
//        if nums:
//        slow = 0
//        for fast in range(1, len(nums)):
//        if nums[fast] != nums[slow]:
//        slow += 1
//        nums[slow] = nums[fast]
//        return slow + 1
//        else:
//        return 0