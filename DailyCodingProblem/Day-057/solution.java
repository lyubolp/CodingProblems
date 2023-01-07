import java.util.ArrayList;
import java.util.List;

/*
Given a string s and an integer k, break up the string into multiple lines such that
    each line has a length of k or less. 
You must break it up so that words don't break across lines. 
Each line has to have the maximum possible amount of words. 
If there's no way to break the text up, then return null.
You can assume that there are no spaces at the ends of the string 
    and that there is exactly one space between each word.
For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
    you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"].
    No string in the list has a length of more than 10.
*/
public class solution {
    public static void main(String[] args) {
        String s = "the quick brown fox jumps over the lazy dog";
        int k = 10;
        List<String> result = breakString(s, k);
        for (String str : result) {
            System.out.println(str);
        }
    }

    private static List<String> breakString(String s, int k) {
        String[] words = s.split(" ");

        List<String> result = new ArrayList<String>();
        
        int i = 0;

        while (i < words.length) {
            String line = "";
            while (i < words.length && line.length() + words[i].length() <= k) {
                line += words[i] + " ";
                i++;
            }
            result.add(line);
        }
        return result;
    }
}
