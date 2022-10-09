use rand::Rng;
use std::{io};

enum Move {
    Rock,
    Paper,
    Scissors,
}

enum Result {
    Win,
    Lose,
    Draw,
}

#[derive(Debug)]
struct Stats {
    wins: u32,
    losses: u32,
    draws: u32,
}
fn main() {
    println!("Rock Paper Scissor\n--------------------------------------------");
    let mut player_stats = Stats { wins: 0, losses: 0, draws: 0 };
    loop {
        begin_game(&mut player_stats);
    }
}

fn begin_game(player_stats: &mut Stats) {
    println!("Choose your move ->\n\t1: Rock\n\t2: Paper\n\t3: Scissor\n--------------------------------------------");
    let user_input:Move = user();
    let c:Move = computer();
    let result:Result = res(user_input, c);
    match result {
        Result::Win => {
            println!("You win!");
            player_stats.wins += 1;
        },
        Result::Lose => {
            println!("You lose!");
            player_stats.losses += 1;
        },
        Result::Draw => {
            println!("Draw!");
            player_stats.draws += 1;
        },
    }    
    println!("\n--------------------------------------------\nWins: {} | Losses: {} | Draws: {}\n--------------------------------------------\n", player_stats.wins, player_stats.losses, player_stats.draws);
}

fn res(u: Move, c: Move) -> Result {
    match u {
        Move::Rock => match c {
            Move::Rock => Result::Draw,
            Move::Paper => Result::Lose,
            Move::Scissors => Result::Win,
        },
        Move::Paper => match c {
            Move::Rock => Result::Win,
            Move::Paper => Result::Draw,
            Move::Scissors => Result::Lose,
        },
        Move::Scissors => match c {
            Move::Rock => Result::Lose,
            Move::Paper => Result::Win,
            Move::Scissors => Result::Draw,
        },
    }
}

fn user() -> Move {
    let mut input:String = String::new();

    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input:u32 = input.trim().parse().expect("Please type a number!");

    print!("You chose: ");
    
    return get_move(input);
}

fn computer() -> Move {
    let random_number:u32 = rand::thread_rng().gen_range(1..4); //generates a random number between 1 and 3

    print!("Computer chose: ");

    return get_move(random_number); 
}

fn get_move(num: u32) -> Move {
    match num {
        1 => {
            println!("Rock");
            return Move::Rock;
        },
        2 => {
            println!("Paper");
            return Move::Paper;
        },
        3 => {
            println!("Scissors");
            return Move::Scissors;
        },
        _ => panic!("Invalid choice!"),
    }
}
