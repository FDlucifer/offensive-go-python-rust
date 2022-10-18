use std::collections::{HashMap, HashSet};
use itertools::Itertools;

#[derive(Debug)]
struct Party {
    happiness_map: HashMap<(String, String), isize>,
    people: HashSet<String>,
}

impl Party {
    fn max_happiness(&self) -> isize {
        let mut max_hap = -100000;
        for seating in self.people.iter().permutations(self.people.len()) {
            let mut hap = 0;
            for (p1, p2) in seating.iter().circular_tuple_windows() {
                //hap += self.happiness_map.get(&(p1.to_string(),p2.to_string())).unwrap_or(&0) +
                //    self.happiness_map.get(&(p2.to_string(), p1.to_string())).unwrap_or(&0);
                hap += self.happiness_map.get(&(p1.to_string(),p2.to_string())).unwrap() +
                    self.happiness_map.get(&(p2.to_string(), p1.to_string())).unwrap();
            }
            if hap > max_hap { max_hap = hap }
        }
        max_hap
    }

    fn add_me(&mut self) {
        for p in self.people.iter() {
            self.happiness_map.insert((p.to_string(), "0xdf".to_string()), 0);
            self.happiness_map.insert(("0xdf".to_string(), p.to_string(), ), 0);
        }
        self.people.insert("0xdf".to_string());
    }
}

impl From<&str> for Party {
    fn from(data: &str) -> Party {
        let mut p = Party {
            happiness_map: HashMap::new(),
            people: HashSet::new(),
        };
        for line in data.lines() {
            let mod_line = line
                .trim_end_matches('.')
                .replace("gain ", "")
                .replace("lose ", "-");
            let tokens: Vec<&str> = mod_line.split(' ').collect();
            let (p1, p2, happiness): (String, String, isize) = (
                tokens[0].to_string(),
                tokens[9].to_string(),
                tokens[2].parse().unwrap(),
            );
            p.happiness_map.insert((p1.clone(), p2), happiness);
            p.people.insert(p1);

        }
        p
    }
}

fn main() {
    let data = include_str!("../input.txt").trim();

    let mut party: Party = data.into();

    println!(
        "Part 1: {}",
        party.max_happiness()
    );

    party.add_me();
    //party.people.insert("0xdf".to_string());

    println!(
        "Part 2: {}",
        party.max_happiness()
    );
}