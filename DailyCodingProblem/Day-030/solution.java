/*
You are given an array of non-negative integers that represents a two-dimensional 
    elevation map where each element is unit-width wall and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
    2 in the second, and 3 in the fourth index 
    (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
*/

/*
              -
              -
    - 0 0 - 0 -
    - 0 0 - 0 -
    - 0 - - 0 -
 */
public class solution {
    public static void main(String[] args) {
        int[] arr = {3, 0, 1, 3, 0, 5};
        System.out.println("The number of units of water trapped is: " + waterTrapped(arr));

        int[] arr2 = {2, 1, 2};
        System.out.println("The number of units of water trapped is: " + waterTrapped(arr2));
    }    

    private static int calculateWaterInRegion(int[] heights, int start, int end) {
        int minArea = Math.min(heights[start], heights[end]);
        int water = 0;

        for (int i = start; i < end; i++) {
            int currentBlock = minArea - heights[i];
            water += currentBlock;
        }
        return water;
    }
    private static int waterTrapped(int[] heights) {
        int water = 0;
        int i = 0;
        while (i < heights.length - 1) {
            for (int j = i + 1; j < heights.length; j++) {
                if (heights[i] <= heights[j]) {
                    water += calculateWaterInRegion(heights, i, j);
                    i = j - 1;
                    break;
                }
            }
            i += 1;
        }

        return water;
    }
}
