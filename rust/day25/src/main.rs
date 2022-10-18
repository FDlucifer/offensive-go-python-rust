use regex::Regex;

fn coord_to_num(r: usize, c: usize) -> usize {
    let tri_base = r + c - 1;
    let tri_count = tri_base * (tri_base + 1) / 2;
    tri_count - r + 1
}

fn num_to_code(num: usize) -> usize {
    (1..num).fold(20151125, |acc, _| (acc * 252533) % 33554393)
}

fn main() {
    let data = include_str!("../input.txt").trim();
    let reg = Regex::new(r"row (\d+), column (\d+)").unwrap();
    let cap = reg.captures(data).unwrap();
    let (r, c): (usize, usize) = (
        cap[1].parse().unwrap(), 
        cap[2].parse().unwrap()
    );

    println!(
        "Part 1: {}",
        num_to_code(coord_to_num(r, c))
    );
}