/*
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
    implement a function rand7() that returns an integer from 1 to 7 (inclusive).
 */

public class solution {
    public static void main(String[] args) {
        System.out.println(rand7());

    }
    
    private static int rand7() {
        double result = rand5() - 1; // [0, 1, 2, 3, 4]
        result = result / 4; // [0, 0.25, 0.5, 0.75, 1]
        result = result * 6; // [0, 1.5, 3, 4.5, 6]

        result += 1; // [1, 2.5, 4, 5.5, 7]
        
        if (result == 2.5) {
            result = middleNumber(2, 3);
        }
        else if (result == 5.5) {
            result = middleNumber(5, 6);
        }

        return (int) result;
    }

    private static int rand5() {
        return (int) (Math.random() * 5) + 1;
    } 
    
    private static int middleNumber(int a, int b) {
        int temp = rand5();
        while (temp != 3) {
            temp = rand5();
        
            if (temp < 3) {
                return a;
            }
            else if (temp > 3) {
                return b;
            }
        }
        return -1;
    }
}
