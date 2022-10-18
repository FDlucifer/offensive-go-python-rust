use itertools::Itertools;
use std::collections::HashMap;
use std::cmp::max;

#[derive(Debug, Clone)]
struct Properties {
    capacity: i64,
    durability: i64,
    flavor: i64,
    texture: i64,
    calories: i64,
}

impl Properties {
    fn new() -> Properties {
        Properties {
            capacity: 0,
            durability: 0,
            flavor: 0,
            texture: 0,
            calories: 0,
        }
    }

    fn add(&mut self, ing: Properties, num: i64) {
        self.capacity += ing.capacity * num;
        self.durability += ing.durability * num;
        self.flavor += ing.flavor * num;
        self.texture += ing.texture * num;
        self.calories += ing.calories * num;
    }

    fn score(&self) -> i64 {
        max(self.capacity, 0) * max(self.durability, 0)
            * max(self.flavor, 0)
            * max(self.texture, 0)
    }
}

#[derive(Debug)]
struct Pantry {
    ingredients: HashMap<String, Properties>,
}

impl Pantry {
    fn best_score(&self) -> (i64, i64) {
        let mut best_score = 0;
        let mut best_500_cal_score = 0;
        for comb in self.ingredients.keys().combinations_with_replacement(100) {
            let mut recipe = Properties::new();
            for (num, i) in comb.iter().dedup_with_count() {
                recipe.add(self.ingredients.get(&i.to_string()).unwrap().clone(), num as i64);
            }
            let score = recipe.score();
            if score > best_score { best_score = score };
            if recipe.calories == 500 && score > best_500_cal_score {
                best_500_cal_score = score;
            }
        }
        (best_score, best_500_cal_score)
    }
}

impl From<&str> for Pantry {
    fn from(s: &str) -> Pantry {
        let mut pantry = Pantry {
            ingredients: HashMap::new(),
        };

        for line in s.lines() {
            let tok: Vec<&str> = line.split(' ').collect();
            let name = tok[0].trim_end_matches(':').to_string();
            pantry.ingredients.insert(
                name,
                Properties {
                    capacity: tok[2].trim_end_matches(',').parse().unwrap(),
                    durability: tok[4].trim_end_matches(',').parse().unwrap(),
                    flavor: tok[6].trim_end_matches(',').parse().unwrap(),
                    texture: tok[8].trim_end_matches(',').parse().unwrap(),
                    calories: tok[10].trim_end_matches(',').parse().unwrap(),
                },
            );
        }
        pantry
    }
}

fn main() {
    let data = include_str!("../input.txt").trim();
    let pantry: Pantry = data.into();

    let (p1, p2) = pantry.best_score();
    println!("Part 1: {}", p1);

    println!("Part 2: {}", p2);
}
