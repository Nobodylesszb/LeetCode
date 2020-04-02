package com.bo.list;

import javax.sound.sampled.SourceDataLine;

public class BestTimeToBuyAndSellStock121 {
    public static int maxProfit(int[] prices){
        int maxCur = 0, maxSofar = 0;
        for(int i =1;i<prices.length;i++){
            maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
            maxSofar = Math.max(maxCur,maxSofar);
        }
        return maxSofar;
    }
    public static void main(String[] args){
        int[] a = {2,-5,5,2,4,5,-3};
        int b ;
        b = maxProfit(a);
        System.out.println(b);      
        
    }

}