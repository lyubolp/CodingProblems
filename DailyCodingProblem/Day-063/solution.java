/*
Given a 2D matrix of characters and a target word, 
    write a function that returns whether the word can be found in the matrix
    by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column. 
Similarly, given the target word 'MASS', you should return true, since it's the last row.
 */
public class solution {
    public static void main(String[] args) {
        char[][] matrix = {
            {'F', 'A', 'C', 'I'},
            {'O', 'B', 'Q', 'P'},
            {'A', 'N', 'O', 'B'},
            {'M', 'A', 'S', 'S'}
        };
        String target = "FOAM";
        System.out.println("Target: " + target + " is present in matrix: " + isPresent(matrix, target));
    }

    private static boolean isPresent(char[][] matrix, String target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int targetLength = target.length();
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == target.charAt(0)) {
                    if (i + targetLength <= rows && isWordVisibleVertical(matrix, target, i, j)) {
                        return true;
                    }
                    else if (j + targetLength <= cols && isWordVisibleHorizontal(matrix, target, i, j)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    private static boolean isWordVisibleVertical(char[][] matrix, String target, int i, int j) {
        int targetLength = target.length();
        for (int k = 0; k < targetLength; k++) {
            if (matrix[i + k][j] != target.charAt(k)) {
                return false;
            }
        }
        return true;
    }

    private static boolean isWordVisibleHorizontal(char[][] matrix, String target, int i, int j) {
        int targetLength = target.length();
        for (int k = 0; k < targetLength; k++) {
            if (matrix[i][j + k] != target.charAt(k)) {
                return false;
            }
        }
        return true;
    }
}
