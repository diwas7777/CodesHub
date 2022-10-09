fn main() {
    let arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let target: i32 = 9;
    testing(&arr, &target); //Given array contains 10 elements and 9 found at index 10
}


fn testing(arr: &[i32], &target: &i32) {
    if let Some(result) = binary_search(&arr, &target) {
        println!("Given array contains {} elements and {} found at index {}", arr.len(), target, result);
    } else {
        println!("{} not found.", target);
    }
}

fn binary_search(arr: &[i32], target: &i32) -> Option<usize> {
    let mut first: usize = 0;
    let mut last: usize = arr.len() - 1;

    while first <= last {
        let midpoint = ((last - first) / 2) + first;
        let midpoint_index = midpoint as usize;
        let val = &arr[midpoint_index];

        if val == target {
            return Some(midpoint_index+1);
        }

        if val < target {
            first = midpoint + 1;
        }

        if val > target {
            last = midpoint - 1;
        }
    }
    None
}
