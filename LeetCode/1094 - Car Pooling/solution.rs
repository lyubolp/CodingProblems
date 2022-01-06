impl Solution {
    pub fn car_pooling(trips: Vec<Vec<i32>>, capacity: i32) -> bool {
        let start: i32 = trips.iter().map(|item| item[1]).min().unwrap();
        let end: i32 = trips.iter().map(|item| item[2]).max().unwrap();
        
        for i in start..=end {
            let mut current_passangers: i32 = 0;
            for trip in &trips{
                if trip[1] <= i && i < trip[2] {
                    current_passangers += trip[0]
                }
            }
            if current_passangers > capacity {
                return false;
            }
        }
        true
    }
}

