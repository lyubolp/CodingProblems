impl Solution {
    pub fn find_min_arrow_shots(points: Vec<Vec<i32>>) -> i32 {
        if points.len() == 0 {
            return 0;
        }
        let mut sorted_points = points.clone();
        
        sorted_points.sort_by(|a, b| a[1].cmp(&b[1]));
        
        let mut arrow: i32 = sorted_points[0][1];
        let mut result: i32 = 1;
        
        for point in sorted_points {
            if point[0] > arrow || arrow > point[1] {
                arrow = point[1];
                result += 1;
            }
        }
        result
    }
}
