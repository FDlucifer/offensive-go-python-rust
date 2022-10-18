use itertools::Itertools;

fn lookandsay(s: String) -> String {
    let mut newstr = String::new();
    for (key, group) in &s.chars().group_by(|c| *c) {
        let num = group.collect::<Vec<_>>().len();

        newstr.push_str(&num.to_string());
        newstr.push(key);
    }
    newstr
}

fn main() {
    let data = include_str!("../input.txt").trim();

    let mut res = data.to_string();
    let mut part1 = 0;

    for i in 0..50 {
        if i == 40 { part1 = res.len(); }
        res = lookandsay(res);
    }

    println!(
        "Part 1: {}",
        part1
    );

    println!(
        "Part 2: {}",
        res.len()
    );
}