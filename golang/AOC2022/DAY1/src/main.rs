fn main() {
    let data = include_str!("../input.txt").trim();
    let mut elves: Vec<usize> = data.split("\n\n")
        .map(|elf| elf.split('\n')
            .map(|e| e.parse::<usize>().unwrap())
            .sum()
        )
        .collect();

    elves.sort();
    elves.reverse();

    println!(
        "Part 1: {}",
        elves[0]
    );

    println!(
        "Part 2: {}",
        elves.iter().take(3).sum::<usize>()
    );
}
