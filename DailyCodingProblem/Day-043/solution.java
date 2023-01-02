import java.util.ArrayList;

/*
Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
 */

class MyStack<T extends Comparable<T>> {
    private ArrayList<T> items;
    private ArrayList<T> maxItems;

    public MyStack() {
        this.items = new ArrayList<T>();
        this.maxItems = new ArrayList<T>();
    }

    public void push(T val) {
        this.items.add(val);

        if (this.maxItems.size() == 0) {
            this.maxItems.add(val);
            return;
        }

        T lastItem = this.maxItems.get(this.maxItems.size() - 1);
        if (val.compareTo(lastItem) > 0) {
            this.maxItems.add(val);
        }
        else {
            this.maxItems.add(lastItem);
        }
    }

    public T pop() {
        if (this.items.size() == 0) {
            return null;
        }
        this.maxItems.remove(this.maxItems.size() - 1);
        return this.items.remove(this.items.size() - 1);
    }

    public T max() {
        return this.maxItems.get(this.maxItems.size() - 1);
    }

    
}
class Solution {
    public static void main(String[] args) { 
        MyStack<Integer> stack = new MyStack<Integer>();

        stack.push(2);
        stack.push(3);
        System.out.println(stack.max()); // 3

        stack.push(1);
        System.out.println(stack.max()); // 3

        stack.push(4);
        System.out.println(stack.max()); // 4

        stack.pop();
        System.out.println(stack.max()); // 3

        stack.pop();
        System.out.println(stack.max()); // 3

        stack.pop();
        System.out.println(stack.max()); // 2
    }

}