fn main() {
    let mut vec:Vec<i32> = vec![3, 2, 5, 1, 4];
    testing(&mut vec); //The sorted array is: [1, 2, 3, 4, 5]
}


fn testing(vec: &mut Vec<i32>) {
  println!("The sorted array is: {:?}", selection_sort(vec));
}

fn selection_sort(vec: &mut Vec<i32>) -> Vec<i32> {
  let mut min: usize = 0;
  let mut temp: i32 = 0;
  for i in 0..vec.len() {
    min = i;
    for j in i+1..vec.len() {
      if vec[j] < vec[min] {
        min = j;
      }
    }
    temp = vec[i];
    vec[i] = vec[min];
    vec[min] = temp;
  }
  return vec.to_vec()
}
