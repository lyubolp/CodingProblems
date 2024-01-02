use std::collections::HashMap;

impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {

        let mut counter: HashMap<i32, u32> = HashMap::new();
        
        for item in nums {
            if counter.contains_key(&item) {
                let current_count = counter.get(&item).unwrap();
                counter.insert(item, current_count + 1);
            }
            else {
                counter.insert(item, 1);
            }
        }

        let mut result: Vec<Vec<i32>> = vec!(vec!());

        for (item, count) in &counter {
            for i in 0..*count {
                if result.len() > i as usize {
                    result[i as usize].push(*item)
                }
                else {
                    result.push(vec![*item]);
                }
            }
        }
        result 
    }
}
