package com.bo.list;

public class bestTimeToBuyAndSell122 {
    public static int maxprofit(int[] prices){
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            profit += Math.max(0,prices[i] - prices[i - 1]);

        }
        return profit;
    }
    public static void main(String[] args){  
        int[] stock = {1,-2,4,-5,6,4};
        int n;
        n = maxprofit(stock);
        System.out.println(n);

    }
}
