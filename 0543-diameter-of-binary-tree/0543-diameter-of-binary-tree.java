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
    public int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        search(root);

        return maxDiameter;
    }

    public int search(TreeNode node) {
        /**
            DFS 탐색
            - 현재 노드를 root로 삼아 가장 긴 diameter 찾아서 현재 Max 값이랑 비교하기
         */

        if (node == null) return 0;

        int left = search(node.left);
        int right = search(node.right);

        maxDiameter = Math.max(maxDiameter, left + right);

        return Math.max(left, right) + 1;
    }
}

