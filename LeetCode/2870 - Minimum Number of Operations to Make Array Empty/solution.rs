use std::collections::{HashMap};

fn min_operations_for_num(x: &i32) -> Option<i32> {
    let possible_operations: Vec<(i32, i32)> = (0..(x / 2) + 1)
        .map(|a| (a, (x - 2 * a) / 3))
        .filter(|(a, b)| 2 * a + 3 * b == *x)
        .collect();

    possible_operations
        .iter()
        .map(|(a, b)| a + b)
        .min()
}

pub fn min_operations(nums: Vec<i32>) -> i32 {

    let mut counter: HashMap<i32, i32> = HashMap::new();
    
    for num in nums {

        let new_count = match counter.get(&num) {
            Some(value) => value + 1,
            None => 1
        };
        counter.insert(num, new_count);
    }

    let operations: Vec<Option<i32>> = counter.values().map(min_operations_for_num).collect();
    
    match operations.iter().filter(|&&operation| operation.is_none()).count() {
        0 => operations.iter().map(|operation| operation.unwrap()).sum(),
        _ => -1
    }
}

fn main() {
    println!("{}", min_operations(vec![2, 3, 3, 2, 2, 4, 2, 3, 4]));
    println!("{}", min_operations(vec![2, 1, 2, 2, 3, 3]));
}
