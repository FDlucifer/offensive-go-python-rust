use fancy_regex::Regex;
use lazy_static::lazy_static;
use std::collections::HashSet;
use itertools::Itertools;

#[derive(Debug)]
struct Password {
    pass: String,
}

impl Password {
    fn new(s: &str) -> Password {
        Password { pass: s.to_string() }
    }

    fn inc(&mut self) {
        let mut chars = self.pass.chars().rev().collect::<Vec<char>>();
        for (i, c) in chars.clone().iter().enumerate() {
            if *c == 'z' {
                chars[i] = 'a'
            } else {
                chars[i] = (chars[i] as u8 + 1) as char;
                self.pass = chars.iter().rev().collect::<String>();
                return;
            }

        }
    }

    fn is_valid(&self) -> bool {
        // can't have i, o, l
        if self.pass.contains('i') || self.pass.contains('o') ||
            self.pass.contains('l') {
                return false
            }

        // must have two different pairs
        lazy_static! {
            static ref RE: Regex = Regex::new(r"(.)\1").unwrap();
        }
        let caps = RE.find_iter(&self.pass)
            .map(|m| m.unwrap().as_str())
            .collect::<HashSet<&str>>();
        if caps.len() < 2 { return false; };

        // must include increasing triplet
        for (a, b, c) in self.pass.chars().tuple_windows() {
            if (a as u8 == b as u8 - 1) && (a as u8 == c as u8 - 2) {
                return true;
            }
        }
        false
    }

    fn next_valid(&mut self) {
        loop {
            self.inc();
            if self.is_valid() { return };
        }
    }
}

impl std::fmt::Display for Password {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}", self.pass)
    }
}

fn main() {
    let data = include_str!("../input.txt").trim();
    let mut p = Password::new(data);

    p.next_valid();
    println!(
        "Part 1: {}",
        p
    );

    p.next_valid();
    println!(
        "Part 2: {}",
        p
    );
}