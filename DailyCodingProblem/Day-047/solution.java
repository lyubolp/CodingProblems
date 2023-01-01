/*
Given a array of numbers representing the stock prices of a company in chronological order, 
    write a function that calculates the maximum profit you could have made 
    from buying and selling that stock once. You must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
    since you could buy the stock at 5 dollars and sell it at 10 dollars.
 * 
 */
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public static void main(String[] args) { 
        String input = readString();
        int[] prices = parseInput(input);

        int[] max_prices = new int[prices.length];
        max_prices[prices.length - 1] = prices[prices.length - 1];

        for (int i = prices.length - 2; i >= 0; i--) {
            max_prices[i] = Math.max(prices[i], max_prices[i + 1]);
        }

        int max_profit = 0;

        for (int i = 0; i < prices.length; i++) {
            max_profit = Math.max(max_profit, max_prices[i] - prices[i]);
        }

        System.out.println(max_profit);
    }

    private static int[] parseInput(String input) {
        String[] items = input.split(" ");

        int[] prices = new int[items.length];
        for(int i = 0; i < items.length; i++) {
            prices[i] = Integer.parseInt(items[i]);
        }

        return prices;
    }
    private static String readString() {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = "";
        try {
            line = reader.readLine();
        }
        catch(Exception e) {
            System.out.println(e);
        }

        return line;
    }
}