/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;
        
        TreeNode newRoot = new TreeNode(root.val);
        invert(root, newRoot);
        return newRoot;
    }

    public void invert(TreeNode originNode, TreeNode newNode){
        if (originNode == null) return;

        if (originNode.right != null){
            newNode.left = new TreeNode(originNode.right.val);
            invert(originNode.right, newNode.left);
        }

        if (originNode.left != null) {
            newNode.right = new TreeNode(originNode.left.val);
            invert(originNode.left, newNode.right);
        }
    }
}