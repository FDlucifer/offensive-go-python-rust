use std::collections::{HashMap,HashSet};

fn main() {
    let data = include_str!("../input.txt").trim();
    let (rep_strs, element) = data.split_once("\n\n").unwrap();

    let map = rep_strs.lines()
        .map(|l| l.split_once(" => ").unwrap())
        .fold(HashMap::<String, Vec<String>>::new(),
            |mut m, (el, new_el)| {
                m.entry(el.to_string())
                    .and_modify(|a| a.push(new_el.to_string()))
                    .or_insert(vec![new_el.to_string()]);
                m
            }
        );
    
    let mut next_elements = HashSet::<String>::new();
    for i in 0..element.len() {
        for j in 1..3 {
            let s = if i <= element.len() - j {
                &element[i..i+j]
            } else {
                ""
            };
            
            match map.get(s) {
                Some(rep) => {
                    for r in rep {
                        let mut new_ele_str = String::new();
                        new_ele_str.push_str(&element[..i]);
                        new_ele_str.push_str(r);
                        new_ele_str.push_str(&element[i+j..]);
                        next_elements.insert(new_ele_str);
                    }
                },
                None => (),
            }
        }
    }
    println!(
        "Part 1: {}",
        next_elements.len()
    );

    let comes_from = data.lines()
        .filter(|l| l.contains("=>"))
        .map(|l| l.split_once(" => ").unwrap())
        .fold(HashMap::<String, String>::new(),
            |mut m, (el, new_el)| {
                m.insert(new_el.to_string(), el.to_string());
            m
        });

    let mut keys = comes_from.keys()
        .into_iter()
        .collect::<Vec<_>>();
    keys.sort_by(|a,b| b.len().cmp(&a.len()));
    
    let mut working = element.clone().to_string();
    let mut count = 0;
    loop {
        for k in keys.iter() {
            if working.contains(*k) {
                let from_e = comes_from.get(*k).unwrap();
                working = working.replacen(*k, &from_e, 1);
                count += 1;
                break;
            }
        }
        if working == "e" { break };
    }
    

    println!(
        "Part 2: {}",
        count
    );
}