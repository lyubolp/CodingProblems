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
    private static int getLength(ListNode head) {
        int length = 0;

        while(head != null) {
            length += 1;
            head = head.next;
        }

        return length;
    }
    private static Stack<Integer> getLastNElements(ListNode head, int amount, int length) {
        Stack<Integer> result = new Stack<Integer>();

        for (int i = 0; i < length; i++) {
            if (i >= length - amount) {
                result.push(head.val);
            }
            head = head.next;
        }

        return result;
    }
    public boolean isPalindrome(ListNode head) {
        int length = getLength(head);
        int mid = length / 2;
        Stack<Integer> items = getLastNElements(head, mid, length);

        for (int i = 0; i < mid; i++) {
            if (head.val != items.pop()) {
                return false;
            }
            head = head.next;
        }

        return true;
    }
}
