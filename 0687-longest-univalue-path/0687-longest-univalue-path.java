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
    public int longest = 0;

    public int longestUnivaluePath(TreeNode root) {
        if (root == null) return 0;
        search(root);

        return longest;
    }

    public int search(TreeNode node) {
        if (node == null) return 0;

        int left = search(node.left);
        int right = search(node.right);

        if (node.left != null && node.val == node.left.val){
            left ++;
        } else left = 0;
        if (node.right != null && node.val == node.right.val){
            right ++;
        } else right = 0;

        longest = Math.max(longest, left + right);

        return Math.max(left, right);
    }

}