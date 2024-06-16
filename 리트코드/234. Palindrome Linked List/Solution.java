import java.util.*;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        Stack<Integer> stack = new Stack<>();

        ListNode node = head;

        while (node != null) {
            stack.push(node.val);
            node = node.next;
        }

        node = head;
        while(node != null){
            if (stack.pop() != node.val){
                return false;
            }
            node = node.next;
        }
        return true;
    }
}