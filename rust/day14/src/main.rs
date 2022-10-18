#[derive(Debug)]
struct Deer {
    _name: String,
    speed: usize,
    move_time: usize,
    rest_time: usize,
    points: usize,
}

impl Deer {
    fn dist_at(&self, t: usize) -> usize {
        let cycle_time = self.move_time + self.rest_time;
        let full_cycles = t / cycle_time;
        let remain_sec = t - (cycle_time * full_cycles);
        if remain_sec > self.move_time {
            (full_cycles + 1) * self.move_time * self.speed
        } else {
            (self.speed * self.move_time * full_cycles) +
                (remain_sec * self.speed)
        }
    }
}

impl Race {
    fn most_dist(&self, t: usize) -> usize {
        self.deer
            .iter()
            .max_by_key(|d| d.dist_at(t))
            .unwrap()
            .dist_at(t)
    }

    fn most_points(&mut self) -> usize {
        for t in 1..2504 {
            let max_dist = self.most_dist(t);
            self.deer
                .iter_mut()
                .filter(|d| d.dist_at(t) == max_dist)
                .for_each(|d| d.points += 1);
        }
        self.deer.iter().max_by_key(|d| d.points).unwrap().points
    }
}

#[derive(Debug)]
struct Race {
    deer: Vec<Deer>,
}

impl From<&str> for Race {
    fn from(s: &str) -> Race {
        let mut race = Race {
            deer: Vec::new(),
        };
        for line in s.lines() {
            let toks: Vec<&str> = line.split(' ').collect();
            race.deer.push( Deer {
                _name: toks[0].to_string(),
                speed: toks[3].parse().unwrap(),
                move_time: toks[6].parse().unwrap(),
                rest_time: toks[13].parse().unwrap(),
                points: 0,
            })
        }
        race
    }
}
    
    
fn main() {
    let data = include_str!("../input.txt").trim();
    let mut race: Race = data.into();
    println!(
        "Part 1: {}",
        race.most_dist(2503)
    );

    println!(
        "Part 2: {}",
        race.most_points()
    );
}