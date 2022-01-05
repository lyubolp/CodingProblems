impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {
        let mut greatest: Vec<i32> = vec!();
        let mut current_max: i32 = -1;
        
        greatest.push(-1);
        
        for item in arr.iter().rev() {
            if item > &current_max {
                current_max = *item;
            }
            
            greatest.push(current_max);
        }
        
        greatest.pop();
        greatest.reverse();
        return greatest;
    }
}