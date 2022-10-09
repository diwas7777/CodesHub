use std::{collections::HashMap, io::stdin, io::Write, io::stdout};
fn main() {
    unf_ck(&read_line());
}

fn read_line() -> String {
    let mut line = String::new();
    print!("Enter the brainf*ck line that you would like to unf*ck: ");
    stdout().flush().unwrap();

    stdin().read_line(&mut line).expect("Error getting line");
    line.truncate(line.trim_end().len());

    return line;
}

fn unf_ck(line: &str) {

    /*
    * This is the brainf*ck interpreter
    * It is a hashmap of text in brainf*ck
    * current_cell_pointer is the current memory cell's pointer
    * loop_brackets is a hashmap of the [] brackets
    * cells is a vector of all cell values
    * current_text_index is the current position in the brainf*ck text
    */

    println!("Unf*cking '{line}' with '{}' characters", line.len());
    print!("Unf*cked text: ");
    
    let loop_brackets:HashMap<usize, usize> = handle_loop_bracket(line);

    let mut current_cell_pointer:usize = 0;
    
    let mut cells: Vec<usize> = Vec::new();
    
    let mut current_text_index:usize = 0;

    while current_text_index < line.len() {
        let c:char = line.chars().nth(current_text_index).unwrap();


        match c {
            '>' => {
                current_cell_pointer += 1;
            }
            '<' => {
                current_cell_pointer -= 1;
            }
            '+' => {
                cells.push(current_cell_pointer);
                cells[current_cell_pointer] = (cells[current_cell_pointer] + 1) % 256
            }
            '-' => {
                cells.push(current_cell_pointer);
                cells[current_cell_pointer] = (cells[current_cell_pointer] - 1) % 256
            }
            '[' => {
                if cells[current_cell_pointer] == 0 {
                    current_text_index = loop_brackets[&current_text_index];
                }
            }
            ']' => {
                if cells[current_cell_pointer] != 0 {
                    current_text_index = loop_brackets[&current_text_index]
                }
            }
            ',' => cells[current_cell_pointer] = c as usize,
            '.' => {
                print!("{}", (cells[current_cell_pointer] as u8) as char)
            }
            _ => {}
        }

        current_text_index += 1;
    }
}

fn handle_loop_bracket(line: &str) -> HashMap<usize, usize> {
    let mut temp: Vec<usize> = Vec::new();
    let mut loop_brackets_res: HashMap<usize, usize> = HashMap::new();

    for (i, c) in line.chars().into_iter().enumerate() {
        match c {
            '[' => temp.push(i),
            ']' => {
                let start:usize = temp.pop().unwrap();
                loop_brackets_res.insert(start, i);
                loop_brackets_res.insert(i, start);
            }

            _ => {}
        }
    }
    loop_brackets_res
}
