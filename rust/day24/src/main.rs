use itertools::Itertools;

fn best_pack(numbers: Vec<usize>, num_spaces: usize) -> usize {
    let total_weight: usize = numbers.iter().sum();

    let mut i = 1;
    let mut min_quantum;
    loop {
        min_quantum = numbers
            .iter()
            .copied()
            .combinations(i)
            .filter(|v| v.iter().sum::<usize>() == total_weight / num_spaces)
            .map(|v| v.iter().fold(1, |q, x| q * x))
            .min();
        if min_quantum != None {
            break;
        }
        i += 1;
    }
    min_quantum.unwrap()
}
fn main() {
    let numbers = include_str!("../input.txt")
        .lines()
        .map(|x| x.parse().unwrap())
        .collect::<Vec<usize>>();

    println!(
        "Part 1: {:?}",
        best_pack(numbers.clone(), 3)
    );

    println!(
        "Part 2: {}",
        best_pack(numbers, 4)
    );
}