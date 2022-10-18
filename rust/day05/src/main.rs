use fancy_regex::Regex;
use lazy_static::lazy_static;

fn nice(s: &str) -> bool {
    lazy_static! {
        static ref RE1: Regex = Regex::new(r"([aeiou].*){3}").unwrap();
        static ref RE2: Regex = Regex::new(r"(.)\1").unwrap();
        static ref RE3: Regex = Regex::new("(ab|cd|pq|xy)").unwrap();
    }
    return RE1.is_match(s).unwrap() &&
           RE2.is_match(s).unwrap() &&
           !RE3.is_match(s).unwrap();
}

/* //bad nice function without lazy static load
fn nice(s: &str) -> bool {
    let re1: Regex = Regex::new(r"([aeiou].*){3}").unwrap();
    let re2: Regex = Regex::new(r"(.)\1").unwrap();
    let re3: Regex = Regex::new("(ab|cd|pq|xy)").unwrap();
    return re1.is_match(s).unwrap() &&
           re2.is_match(s).unwrap() &&
           !re3.is_match(s).unwrap();
} */


fn nice2(s: &str) -> bool {
    lazy_static! {
        static ref RE4: Regex = Regex::new(r"(..).*\1").unwrap();
        static ref RE5: Regex = Regex::new(r"(.).\1").unwrap();
    }
    return RE4.is_match(s).unwrap() &&
           RE5.is_match(s).unwrap();
}

fn main() {
    let data = include_str!("../input.txt");

    let part1 = data
        .lines()
        .filter(|line| nice(line))
        .count();

    println!(
        "Part 1: {}",
        part1
    );

    let part2 = data
        .lines()
        .filter(|line| nice2(line))
        .count();

    println!(
        "Part 2: {}",
        part2
    );
}