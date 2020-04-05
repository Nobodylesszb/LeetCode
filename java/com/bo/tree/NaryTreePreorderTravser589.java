package com.bo.tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class NaryTreePreorderTravser589 {
    
    //迭代解法
    public List<Integer> preorder(Node root){
        List<Integer> list = new ArrayList<>();
        if (root == null) return list;
        Stack<Node> stack = new Stack<>();
        stack.add(root);
        while(!stack.empty()){
            root = stack.pop();
            list.add(root.val);
            for(int i = root.children.size() - 1; i >= 0; i--){
                stack.add(root.children.get(i));
            }
        }
        return list;
    }

    public List<Integer> list = new ArrayList<>();

    //递归解法
    public List<Integer> preorder2(Node root){
        if(root == null) return list;
        list.add(root.val);
        for(Node node : root.children){
            preorder(node);
        }
        return list;
    }
}