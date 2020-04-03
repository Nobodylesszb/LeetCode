package com.bo.string;

/**
 * @Auther: bo
 * @Date: 2020/4/2 23:08
 * @Version:
 * @Description:
 */
public class SplitStringInBalanceString1221 {
    public int balancedStringSplit(String s) {
       int res =0,cnt =0;
        for (int i = 0; i <s.length(); i++) {
            cnt += s.charAt(i) == 'L' ? 1 : -1;
            if (cnt == 0)
                ++res;

        }

        return res;
    }
}
