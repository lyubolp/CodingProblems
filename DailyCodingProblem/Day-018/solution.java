import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;

/*
Given an array of integers and a number k, where 1 <= k <= length of the array, 
    compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place 
    and you do not need to store the results. You can simply print them out as you compute them.
 */

class Pair<T, U> {
    private T first;
    private U second;

    public Pair(T first, U second) {
        this.first = first;
        this.second = second;
    }

    public T getFirst() {
        return first;
    }

    public U getSecond() {
        return second;
    }
};

class MaxQueue {
    Stack<Pair<Integer, Integer>> first = new Stack<Pair<Integer, Integer>>();
    Stack<Pair<Integer, Integer>> second = new Stack<Pair<Integer, Integer>>();

    public void enqueue(int item) {
        if (first.isEmpty()) {
            first.push(new Pair<Integer, Integer>(item, item));
        } else {
            first.push(new Pair<Integer, Integer>(item, Math.max(item, first.peek().getSecond())));
        }
    }

    public Integer dequeue() {
        if (second.isEmpty()) {
            while (!first.isEmpty()) {
                Integer item = first.pop().getFirst();

                if (second.isEmpty()) {
                    second.push(new Pair<Integer, Integer>(item, item));
                } else {
                    second.push(new Pair<Integer, Integer>(item, Math.max(item, second.peek().getSecond())));
                }
            }
        }

        return second.pop().getFirst();
    }

    public Integer getMaxValue() {
        if (first.isEmpty()) {
            return second.peek().getSecond();
        } else if (second.isEmpty()) {
            return first.peek().getSecond();
        } else {
            return Math.max(first.peek().getSecond(), second.peek().getSecond());
        }
    }

    public void print() {
        for (Pair<Integer, Integer> item: second) {
            System.out.print(item.getFirst());
            System.out.print(" ");
        }
        System.out.print("/ ");
        for (Pair<Integer, Integer> item: first) {
            System.out.print(item.getFirst());
            System.out.print(" ");
        }
        
        System.out.println();
    }
};
public class solution {
    public static void main(String[] args) {
        Integer[] arr = {10, 5, 2, 7, 8, 7};
        int k = 3;

        Integer[] result = calculateSubArraySum(arr, k);

        for (Integer item: result) {
            System.out.print(item);
            System.out.print(" ");
        }
    }

    private static Integer[] calculateSubArraySum(Integer[] arr, int k) {
        Integer[] result = new Integer[arr.length - k + 1];

        MaxQueue queue = new MaxQueue();

        for(int i = 0; i < k; i++) {

            queue.enqueue(arr[i]);
        }
        
        result[0] = queue.getMaxValue();
        queue.print();

        for(int i = k; i < arr.length; i++) {
            queue.dequeue();
            queue.enqueue(arr[i]);
            queue.print();

            Integer maxValue = queue.getMaxValue();
            System.out.println("maxValue: " + maxValue);
            result[i - k + 1] = maxValue;
        }
        return result;
    }
}
