use std::collections::HashMap;
use std::str::FromStr;

#[derive(Debug)]
struct Lights {
    grid: HashMap<(isize, isize), bool>,
    rows: usize,
    cols: usize,
}

impl Lights {
    fn next(&mut self) {
        let mut next_grid: HashMap<(isize, isize), bool> = HashMap::new();
        for r in 0..self.rows as isize {
            for c in 0..self.cols as isize {
                let current = *self.grid.get(&(r,c)).unwrap();
                let num_neighbors = self.count_neighbors(r, c);
                let next = (current && [2,3].contains(&num_neighbors)) || 
                    (!current && num_neighbors == 3);
                next_grid.insert((r,c), next);
                //if r == 0 && c < 15 {println!("[{r},{c}] {current} {num_neighbors} {next}")};
            }
        }
        self.grid = next_grid;
    }

    fn count_neighbors(&self, r: isize, c: isize) -> usize {
        let mut num_on = 0;
        for dr in -1..2 {
            for dc in -1..2 {
                if dr == 0 && dc == 0 { continue };
                if *self.grid.get(&(r+dr,c+dc)).unwrap_or(&false) {
                    num_on += 1;
                }
            }
        }
        num_on
    }

    fn run_steps(&mut self, num_steps: usize, p2: bool) {
        if p2 { self.corners_on() };
        for _ in 0..num_steps {
            self.next();
            if p2 { self.corners_on() };
        }
    }

    fn count_on(&self) -> usize {
        self.grid
            .values()
            .filter(|b| **b)
            .count()
    }

    fn corners_on(&mut self) {
        [(0,0), (0,(self.cols-1) as isize), ((self.rows-1) as isize,0), ((self.rows-1) as isize,(self.cols-1) as isize)].iter().for_each(
            |p| { self.grid.insert(*p, true);
        })
    }
}

impl FromStr for Lights {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut lights = Self {
            grid: HashMap::new(),
            rows: s.lines().count(),
            cols: s.lines().next().unwrap().chars().count(),
        };
        for (r, line) in s.lines().enumerate() {
            for (c, ch) in line.chars().enumerate() {
                lights.grid.insert((r as isize, c as isize), ch == '#');
            }
        }
        Ok(lights)
    }
}

fn main() {
    let data = include_str!("../input.txt").trim();
    let mut lights: Lights = data.parse().unwrap();

    lights.run_steps(100, false);
    println!(
        "Part 1: {:?}",
        lights.count_on()
    );

    let mut lights2: Lights = data.parse().unwrap();
    lights2.run_steps(100, true);

    println!(
        "Part 2: {}",
        lights2.count_on()
    );
}