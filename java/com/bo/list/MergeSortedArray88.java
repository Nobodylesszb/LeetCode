package com.bo.list;

/**
 * @Auther: bo
 * @Date: 2020/4/2 17:32
 * @Version:
 * @Description:
 */
public class MergeSortedArray88 {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m-1, j = n-1,k = m+n-1;
        while (i >=0 && j>=0){
            nums1[k--] = nums1[i]>nums2[j]?nums1[i--]:nums2[j--];
        }
        while (j>=0){
            nums1[k--] =nums2[j--];
        }

    }

    public static void main(String[] args) {
        int [] a = {1,3,4,5};
        int [] b = {2,4,5,6};
        merge(a,5,b,5);
        System.out.println(a.toString());
    }

}
