use itertools::iproduct;

struct Character {
    hit_points: usize,
    damage: usize,
    armor: usize,
    cost: usize,
}

impl Character {
    fn new(w: &Item, a: &Item, r1: &Item, r2: &Item, hp: usize) -> Self {
        Self {
            hit_points: hp,
            damage: w.damage + a.damage + r1.damage + r2.damage,
            armor: w.armor + a.armor + r1.armor + r2.armor,
            cost: w.cost + a.cost + r1.cost + r2.cost,
        }
    }

    fn defeats(&self, boss: &Character) -> bool {
        let my_turns_to_win = div_ceil(boss.hit_points, 
            calc_damage(self.damage, boss.armor));
        let boss_turns_to_win = div_ceil(self.hit_points,
             calc_damage(boss.damage, self.armor));
        my_turns_to_win <= boss_turns_to_win
    }
}

fn calc_damage(damage: usize, armor: usize) -> usize {
    if damage > armor {
        damage - armor
    } else {
        1
    }
}

fn div_ceil(a: usize, b: usize) -> usize {
    (a / b) + usize::from(a % b != 0)
}

struct Item {
    name: String,
    cost: usize,
    damage: usize,
    armor: usize,
}

fn main() {
    let boss = Character {
        hit_points: 109,
        damage: 8,
        armor: 2,
        cost: 0,
    };

    let weapons = [
        Item { name: "Dagger".to_string(), cost: 8, damage: 4, armor: 0 },
        Item { name: "Shortsword".to_string(), cost: 10, damage: 5, armor: 0 },
        Item { name: "Warhammer".to_string(), cost: 25, damage: 6, armor: 0 },
        Item { name: "Longsword".to_string(), cost: 40, damage: 7, armor: 0 },
        Item { name: "Greataxe".to_string(), cost: 74, damage: 8, armor: 0 },
    ];
    let armors = [
        Item { name: "none".to_string(), cost: 0, damage: 0, armor: 0},
        Item { name: "Leather".to_string(), cost: 13, damage: 0, armor: 1 },
        Item { name: "Chainmail".to_string(), cost: 31, damage: 0, armor: 2 },
        Item { name: "Splintmail".to_string(), cost: 53, damage: 0, armor: 3 },
        Item { name: "Bandedmail".to_string(), cost: 75, damage: 0, armor: 4 },
        Item { name: "Platemail".to_string(), cost: 102, damage: 0, armor: 5 },
    ];
    let rings = [
        Item { name: "none".to_string(), cost: 0, damage: 0, armor: 0},
        Item { name: "Damage +1".to_string(), cost: 25, damage: 1, armor: 0 },
        Item { name: "Damage +2".to_string(), cost: 50, damage: 2, armor: 0 },
        Item { name: "Damage +3".to_string(), cost: 100, damage: 3, armor: 0 },
        Item { name: "Defense +1".to_string(), cost: 20, damage: 0, armor: 1 },
        Item { name: "Defense +2".to_string(), cost: 40, damage: 0, armor: 2 },
        Item { name: "Defense +3".to_string(), cost: 80, damage: 0, armor: 3 },
    ];

    let cheapest_win = iproduct!(&weapons, &armors, &rings, &rings)
        .filter(|(_, _, r1, r2)| {
            r1.name != r2.name || r1.name == "none".to_string()
        })
        .map(|(w, a, r1, r2)| {
            Character::new(&w, &a, &r1, &r2, 100)
        })
        .filter(|f| { f.defeats(&boss) })
        .min_by(|a, b| a.cost.cmp(&b.cost))
        .unwrap();

    println!(
        "Part 1: {}",
        cheapest_win.cost
    );

    let expensive_loss = iproduct!(&weapons,&armors,&rings,&rings)
        .filter(|(_, _, r1, r2)| { 
            r1.name == "none".to_string() || r1.name != r2.name 
        })
        .map(|(w, a, r1, r2)| {
            Character::new(&w, &a, &r1, &r2, 100)
        })
        .filter(|f| { ! f.defeats(&boss) })
        .max_by(|a, b| a.cost.cmp(&b.cost))
        .unwrap();

    println!(
        "Part 2: {}",
        expensive_loss.cost
    );
}