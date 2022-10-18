use itertools::Itertools;

fn main() {
    let sizes: Vec<usize> = include_str!("../input.txt")
        .lines()
        .map(|x| x.parse().unwrap())
        .collect();

    let mut num_valid_combos = 0;
    let mut part2 = 0;
    for i in 1..sizes.len() {
        let c = sizes.iter()
            .combinations(i)
            .filter(|comb| comb.into_iter().copied().sum::<usize>() == 150)
            .count();
        num_valid_combos += c;
        if part2 == 0 && c > 0 {
            part2 = c;
        }
    }
    println!(
        "Part 1: {}",
        num_valid_combos
    );

    println!(
        "Part 2: {}",
        part2
    );
}