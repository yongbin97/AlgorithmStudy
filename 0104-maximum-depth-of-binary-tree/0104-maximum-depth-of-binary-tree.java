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
    public int maxDepth(TreeNode root) {
        int answer = 0;

        if (root == null) return answer;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()){
            queue = getChildren(queue);
            answer ++;
        }
        return answer;
    }

    public Queue<TreeNode> getChildren(Queue<TreeNode> parents){
        Queue<TreeNode> children = new LinkedList<>();

        while (!parents.isEmpty()){
            TreeNode node = parents.poll();

            if (node.left != null) children.add(node.left);
            if (node.right != null) children.add(node.right);
        }

        return children;
    }
}