import java.util.Arrays;

/*
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
    find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
 */
public class solution {
    public static void main(String[] args) {
        Integer[][] arr = {{30, 75}, {0, 50}, {60, 150}};

        System.out.println("Minimum number of rooms required: " + calculateRooms(arr));
    }

    private static int calculateRooms(Integer[][] lectures) {
        Arrays.sort(lectures, (a, b) -> a[0] - b[0]);

        for (Integer[] lecture: lectures) {
            System.out.println(Arrays.toString(lecture));
        }

        int rooms = 0;
        
        for (int i = 0; i < lectures.length; i++) {
            if (lectures[i][0] < lectures[i][1]) {
                rooms++;
            }
        }
        return rooms;
    }
}
