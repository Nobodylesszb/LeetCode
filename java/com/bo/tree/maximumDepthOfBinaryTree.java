package com.bo.tree;

import java.util.LinkedList;
import java.util.Queue;

public class maximumDepthOfBinaryTree {
    public int maxDepth(TreeNode root){
        if (root == null){
            return 0;
        }
        return 1 + Math.max(maxDepth(root.left),maxDepth(root.right));
    }

    //iterative

    public int maxDepth2(TreeNode root){
        if (root == null) return 0;
        
        int depth = 0;
        Queue<TreeNode> nodes = new LinkedList<>();
        nodes.offer(root);
        while (!nodes.isEmpty()) {
            int size = nodes.size();
            depth++;
            while (size-- > 0) {
                TreeNode node = nodes.poll();
                if (node.left != null) nodes.offer(node.left);
                if (node.right != null) nodes.offer(node.right);
            }
        }
        return depth;
    }
}