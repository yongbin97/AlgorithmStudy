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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        return merge(root1, root2);
    }

    public TreeNode merge(TreeNode node1, TreeNode node2){
        if (node1 == null && node2 == null) return null;

        TreeNode newNode = new TreeNode();
        if (node1 != null) newNode.val += node1.val;
        if (node2 != null) newNode.val += node2.val;

        TreeNode left1 = node1 != null ? node1.left : null;
        TreeNode left2 = node2 != null ? node2.left : null;
        TreeNode right1 = node1 != null ? node1.right : null;
        TreeNode right2 = node2 != null ? node2.right : null;

        newNode.left = merge(left1, left2);
        newNode.right = merge(right1, right2);

        return newNode;
    }
}