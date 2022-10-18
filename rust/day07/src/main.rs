use std::collections::HashMap;

#[derive(Debug, Clone)]
struct Gate {
    in1: String,
    in2: String,
    op: String,
}

impl From<&str> for Gate {
    fn from(s: &str) -> Gate {
        let s_vec: Vec<&str> = s.split(' ').collect();
        if s_vec[0] == "NOT" {
            Gate {
                op: s_vec[0].to_string(),
                in1: s_vec[1].to_string(),
                in2: "".to_string()
            }
        } else if s_vec.len() == 1 {
            Gate {
                op: "NONE".to_string(),
                in1: s_vec[0].to_string(),
                in2: "".to_string(),
            }
        } else {
            Gate {
                op: s_vec[1].to_string(),
                in1: s_vec[0].to_string(),
                in2: s_vec[2].to_string(),
            }
        }

    }
}

struct Challenge {
    commands: HashMap<String, Gate>,
    values: HashMap<String, u16>,
}

impl Challenge {
    fn new() -> Self {
        Self {
            commands: HashMap::new(),
            values: HashMap::new(),
        }
    }

    fn get_value(&mut self, node: String) -> u16 {
        if node.chars().all(|c| c.is_ascii_digit()) {
            return node.parse::<u16>().unwrap();
        }
        if self.values.contains_key(&node) {
            return *self.values.get(&node).unwrap();
        }

        let g = self.commands.get(&node).unwrap().clone();
        let v1 = self.get_value(g.in1);
        let op = g.op.as_str();
        let result = match op {
            "NONE" => v1,
            "NOT" => ! v1,
            _ => {
                let v2 = self.get_value(g.in2);
                match op {
                    "OR" => v1 | v2,
                    "AND" => v1 & v2,
                    "LSHIFT" => v1 << v2,
                    "RSHIFT" => v1 >> v2,
                    _ => panic!("Unhandled op {}", g.op),
                }
            }
        };
        self.values.insert(node.to_string(), result);
        result
    }

    fn reset_part2(&mut self, part1: u16) {
        self.commands.entry("b".to_string()).and_modify(|x| {
            x.in1 = part1.to_string();
            x.in2 = "".to_string();
            x.op = "NONE".to_string();
        });
        self.values = HashMap::new();
    }
}

fn main() {
    let data = include_str!("../input.txt");
    let mut chal = Challenge::new();
    
    for line in data.lines() {
        let (input, output) = line.split_once(" -> ").unwrap();
        chal.commands.insert(output.to_string(), input.into());
    }
    
    let part1 = chal.get_value("a".to_string());
    println!(
        "Part 1: {}",
        part1
    );

    chal.reset_part2(part1);
    println!(
        "Part 2: {}",
        chal.get_value("a".to_string())
    );
}