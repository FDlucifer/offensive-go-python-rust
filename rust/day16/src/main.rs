use std::collections::HashMap;

#[derive(Debug,Clone)]
struct Sue {
    id: usize,
    props: HashMap<String, usize>,
}

impl Sue {
    fn matches(&self, s: Sue) -> bool {
        for (prop, num) in s.props.iter() {
            if self.props.get(prop).unwrap() != num {
                return false;
            }
        }
        true
    }

    fn matches2(&self, s: Sue) -> bool {
        for (prop, num) in s.props.iter() {

            if ["cats", "trees"].contains(&prop.as_str()) {
                if self.props.get(prop).unwrap() >= num {
                    return false;
                }
            } else if ["pomeranians", "goldfish"].contains(&prop.as_str()) {
                if self.props.get(prop).unwrap() <= num {
                    return false;
                }
            } else {
                if self.props.get(prop).unwrap() != num {
                    return false;
                }
            }
        }
        true
    }
}

impl From<&str> for Sue {
    fn from(s: &str) -> Sue {
        // Sue 2: perfumes: 5, trees: 8, goldfish: 8
        let toks: Vec<&str> = s.split(' ').collect();
        let mut sue = Sue {
            id: toks[1].trim_end_matches(':').parse().unwrap(),
            props: HashMap::new(),
        };
        let mut i = 2;
        while i < toks.len() {
            let item = toks[i].trim_end_matches(':').to_string();
            let num = toks[i+1].trim_end_matches(',').parse().unwrap();
            sue.props.insert(item, num);
            i += 2;
        }
        sue
    }
}

fn main() {
    let data = include_str!("../input.txt").trim();
    let default_sue_str = "Sue 0: children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1";
    let sue: Sue = default_sue_str.into();

    for line in data.lines() {
        let maybe_sue: Sue = line.into();
        if sue.matches(maybe_sue.clone()) {
            println!("Part 1: {}", maybe_sue.id);
        }
        if sue.matches2(maybe_sue.clone()) {
            println!("Part 1: {}", maybe_sue.id);
        }
    }
}