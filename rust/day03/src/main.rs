use std::collections::HashMap;

fn main() {
    let data = include_str!("../input.txt");

    let mut pos = (0,0);
    let mut houses = HashMap::new();
    houses.insert(pos, 1);

    let mut santa = (0,0);
    let mut robot = (0,0);
    // https://stackoverflow.com/questions/29672373/what-is-difference-between-mut-a-t-and-a-mut-t
    let mut current: &mut (i32, i32);
    let mut houses2 = HashMap::new();
    houses2.insert(santa, 2);

    for (i, c) in data.chars().enumerate() {
        current = if i % 2 == 0 { &mut santa } else { &mut robot };
        match c {
            '>' => {
                pos.0 += 1;
                current.0 += 1;
            },
            '^' => {
                pos.1 += 1;
                current.1 += 1;
            },
            '<' => {
                pos.0 -= 1;
                current.0 -= 1;
            },
            'v' => {
                pos.1 -= 1;
                current.1 -= 1;
            },
            _ => panic!("Invalid input"),
        };
        houses.entry(pos).and_modify(|h| *h += 1).or_insert(1);
        houses2.entry(*current).and_modify(|h| *h += 1).or_insert(1);
    }

    println!(
        "Part 1: {}",
        houses.len()
    );

    println!(
        "Part 2: {}",
        houses2.len()
    );
}