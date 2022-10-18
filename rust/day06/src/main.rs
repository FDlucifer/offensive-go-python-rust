use regex::Regex;

struct Instruction {
    instruction: String,
    start: Vec<usize>,
    end: Vec<usize>,
}

impl From<&str> for Instruction {
    fn from(s: &str) -> Instruction {
        let parser = Regex::new(
            r"(?P<inst>turn off|turn on|toggle) (?P<start>\d+,\d+) through (?P<end>\d+,\d+)",
        )
        .unwrap();
    
        let captures = parser.captures(s).ok_or("no matches").unwrap();
        let instruction = captures.name("inst").map_or("", |m| m.as_str()).to_string();
        let start: Vec<usize> = captures
            .name("start")
            .map_or("", |m| m.as_str())
            .split(',')
            .map(|s| s.parse().expect("Parse error: {s} not an int"))
            .collect();
        let end: Vec<usize> = captures
            .name("end")
            .map_or("", |m| m.as_str())
            .split(',')
            .map(|s| s.parse().expect("Parse error: {s} not an int"))
            .collect();
        Instruction { instruction, start, end }
    }
}


#[derive(Debug)]
struct Grid {
    grid: [[u8; 1000]; 1000],
}

impl Grid {
    fn new() -> Self {
        Self { grid: [[0u8; 1000]; 1000]}
    }

    fn process_instruction(&mut self, inst: &Instruction) {
        for r in inst.start[0]..inst.end[0]+1 {
            for c in inst.start[1]..inst.end[1]+1 {
                match inst.instruction.as_str() {
                    "turn on" => self.grid[r][c] = 1,
                    "turn off" => self.grid[r][c] = 0,
                    "toggle" => self.grid[r][c] = (self.grid[r][c] + 1) % 2,
                    _ => panic!("Unexpected instfuction {}", inst.instruction),
                }
            }
        }
    }

    fn process_instruction2(&mut self, inst: &Instruction) {
        for r in inst.start[0]..inst.end[0]+1 {
            for c in inst.start[1]..inst.end[1]+1 {
                match inst.instruction.as_str() {
                    "turn on" => self.grid[r][c] += 1,
                    "turn off" => {
                        if self.grid[r][c] > 0 {
                            self.grid[r][c] -= 1
                        }
                    },
                    "toggle" => self.grid[r][c] += 2,
                    _ => panic!("Unexpected instfuction {}", inst.instruction),
                }
            }
        }
    }

    fn sum_lights(&self) -> usize {
        self.grid
            .iter()
            .fold(0, |acc, row| {
                acc + row.iter().fold(0, |inner_acc, cell| inner_acc + *cell as usize) as usize
            })
    }
}

fn main() {
    let data = include_str!("../input.txt");
    let mut g = Grid::new();
    let mut g2 = Grid::new();

    for line in data.lines() {
        let inst: Instruction = line.into();
        g.process_instruction(&inst);
        g2.process_instruction2(&inst);
    }

    println!("Part 1: {}", g.sum_lights());

    println!("Part 2: {:?}", g2.sum_lights());
}
