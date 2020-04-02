package com.bo.string;

import java.util.Stack;

/**
 * @Auther: bo
 * @Date: 2020/4/2 13:17
 * @Version:
 * @Description:
 */
public class validParentheses20 {
    public static boolean isValid(String s){
        char[] str = s.toCharArray();
        Stack<Character> stack = new Stack<Character>();
        char check;
        for (char c:str){
            if(c == '{' || c == '[' || c == '('){
                stack.push(c);
            }
            else {
                if(!stack.isEmpty()){
                    check = stack.pop();
                    if (c == '}' && check != '{') {
                        return false;
                    } else if (c == ']' && check != '[') {
                        return false;
                    } else if (c == ')' && check != '(') {
                        return false;
                    }
                }else {
                    return  false;
                }
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String s = "([)]";
        boolean t = isValid(s);
        System.out.println(t);
    }
}
