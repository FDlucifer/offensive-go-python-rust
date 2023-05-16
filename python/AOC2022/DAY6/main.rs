use std::collections::HashSet;

fn get_marker(data: &str, size: usize) -> usize {
    data.as_bytes()
        .windows(size)
        .position(|w| HashSet::<&u8>::from_iter(w).len() == size)
        .unwrap() + size
}

fn main() {
    let data = include_str!("input.txt").trim();

    println!(
        "part 1: {}",
        get_marker(data, 4)
    );

    println!(
        "part 2: {}",
        get_marker(data, 14)
    );
}
