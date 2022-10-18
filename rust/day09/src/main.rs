use std::collections::{HashMap, HashSet};
use itertools::Itertools;

fn main() {
    let data = include_str!("../input.txt");
    let mut routes: HashMap<(String, String), u32> = HashMap::new();
    let mut cities = HashSet::new();

    for line in data.lines() {
        let tokens: Vec<&str> = line.split(' ').collect();
        let (c1, c2, dist) = (
            tokens[0].to_string(),
            tokens[2].to_string(),
            tokens[4].parse().unwrap(),
        );
        routes.insert((c1.clone(), c2.clone()), dist);
        routes.insert((c2.clone(), c1.clone()), dist);
        cities.insert(c1);
        cities.insert(c2);
    }

    let mut min_distance = 100000000;
    let mut max_distance = 0;
    for route in cities.iter().permutations(cities.len()) {
        let mut dist = 0;
        /*let mut it = route.iter();
        let mut c1 = it.next().unwrap();
        while let Some(c2) = it.next() {
            dist += *routes
                .get(&(c1.to_string(), c2.to_string()))
                .unwrap();
            c1 = c2;
        } */
        for (c1, c2) in route.iter().tuple_windows() {
            dist += routes.get(&(c1.to_string(), c2.to_string())).unwrap();
        }
        if dist < min_distance { min_distance = dist };
        if dist > max_distance {max_distance = dist};
    } 
    println!(
        "Part 1: {:?}",
        min_distance
    );

    println!(
        "Part 2: {:?}",
        max_distance
    );
}