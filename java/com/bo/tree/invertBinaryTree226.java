package com.bo.tree;

import java.util.LinkedList;
import java.util.Queue;

public class invertBinaryTree226 {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }

        final Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()) {
            final TreeNode node = queue.poll();
            final TreeNode left = node.left;
            node.left = node.right;
            node.right = left;

            if(node.left != null) {
                queue.offer(node.left);
            }
            if(node.right != null) {
                queue.offer(node.right);
            }
        }
        return root;
    }

    public TreeNode invertTree2(TreeNode root) {
        if (root == null) return null;
        TreeNode tempRight = root.right;
        root.right = invertTree(root.left);
        root.left = invertTree(tempRight);
        return root;
    }

}