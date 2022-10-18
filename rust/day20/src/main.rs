/* fn sum_of_factors(n: usize) -> usize {
    (1..n+1).into_iter()
        .filter(|x| n % x == 0)
        .sum()
} */

fn main() {
    let min_presents = include_str!("../input.txt")
        .trim()
        .parse::<usize>()
        .unwrap();

    // slow way, CPU heavy
    /* let mut i = 1;
    while sum_of_factors(i) * 10 < _min_presents {
        i += 1;

    println!("{}", i);
    } */

    let mut houses = vec![0; min_presents/10];

    for elf_id in 1..houses.len() {
        let mut loc = elf_id;
        while loc < houses.len() {
            houses[loc] += elf_id * 10;
            loc += elf_id;
        }
    }

    println!(
        "Part 1: {}",
        houses.iter().position(|x| x >= &min_presents).unwrap()
    );

    let mut houses2 = vec![0; min_presents/11];

    for elf_id in 1..houses2.len() {
        let mut loc = elf_id;
        let mut delivered = 0;
        while loc < houses2.len() && delivered < 50 {
            houses2[loc] += elf_id * 11;
            loc += elf_id;
            delivered += 1;
        }
    }

    println!(
        "Part 2: {}",
        houses2.iter().position(|x| x >= &min_presents).unwrap()
    );
}