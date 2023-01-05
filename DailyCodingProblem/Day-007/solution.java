import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Stack;

/*
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
 */

public class solution {
    public static void main(String[] args) {
        String message = "111";
        System.out.println(countWays(message));
    }

    //111 -> 1;11 or 11;1
    //1;11 -> 1;1;1 or 1;11
    //11;1 -> 1;1;1 or 11;1

    private static int countWays(String message) {
        Stack<List<String>> stack = new Stack<>();
        HashSet<String> results = new HashSet<>();

        stack.push(List.of("", message));

        while(!stack.isEmpty()) {
            List<String> current = stack.pop();
            String soFar = current.get(0);
            String left = current.get(1);
            
            if (left.length() == 0) {
                System.out.println(soFar);
                results.add(soFar);
                continue;
            }
            
            if (left.charAt(0) == '0') {
                //Take no chars
                continue;
            }

            boolean canTakeTwoStartingWithOne = left.charAt(0) == '1' && left.length() > 1;
            boolean canTakeTwoStartingWithTwo = left.charAt(0) == '2' && left.length() > 1 && left.charAt(1) <= '6';
            if (canTakeTwoStartingWithOne || canTakeTwoStartingWithTwo) {
                String two = left.substring(0, 2);
                stack.push(List.of(soFar + decode(two), left.substring(2)));
            }
            
            //Take one char
            String one = left.substring(0, 1);
            stack.push(List.of(soFar + decode(one), left.substring(1)));
        
        }
        return results.size();
    } 
    private static String decode(String message) {
        int number = Integer.parseInt(message);
        return Character.toString((char) (number + 96));
    }
}
