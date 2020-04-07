package com.bo.tree;

public class leafSimilarTree872 {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        StringBuilder root1Leaves = new StringBuilder(),root2Leaves=new StringBuilder();
        traverse(root1,root1Leaves);traverse(root2,root2Leaves);	    
		return root1Leaves.toString().equals(root2Leaves.toString());
    }
    
    //获得叶子节点
    public void traverse(TreeNode root,StringBuilder recordLeaves){
        if(root==null) return;
        if(root.left==null && root.right==null) recordLeaves.append(root.val+"-");
        traverse(root.left, recordLeaves);
        traverse(root.right, recordLeaves);
    }
}