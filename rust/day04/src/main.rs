use std::env;
use md5;

fn solve(key: &str, num_zeros: usize, start: u32) -> u32 {
    let mut i = start;

    loop {
        let s = format!("{key}{i}");
        let h = format!("{:x}", md5::compute(s));
        if &h[..num_zeros] == format!("{:0num_zeros$}", 0) {
            return i;
        }
        i += 1;
    }
}

fn main() {
    let data = include_str!("../input.txt").trim();
    let args: Vec<String> = env::args().collect();
    let key = if args.len() == 1 { data } else { &args[1] };

    let part1 = solve(key, 5, 1);
    println!(
        "Part 1: {}",
        part1
    );

    println!(
        "Part 2: {}",
        solve(key, 6, part1)
    );
}