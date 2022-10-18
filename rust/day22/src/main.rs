use std::collections::VecDeque;

#[derive(Debug, Clone, Copy)]
enum Spell {
    Missile,
    Drain,
    Shield,
    Poison,
    Recharge,
}

#[derive(Debug, Clone, Copy)]
struct Game {
    p_hp: isize,
    p_mp: isize,
    p_armor: isize,
    b_hp: isize,
    b_damage: isize,
    mana_spent: usize,
    shield: u8,
    poison: u8,
    recharge: u8,
}

fn fight(state: Game, hard: bool) -> usize {
    // init queue and result
    let mut smallest_mana = usize::MAX;
    let mut queue = VecDeque::new();

    queue.push_back((state, Spell::Missile));
    queue.push_back((state, Spell::Drain));
    queue.push_back((state, Spell::Shield));
    queue.push_back((state, Spell::Poison));
    queue.push_back((state, Spell::Recharge));

    // loop
    while let Some((mut state, next_spell)) = queue.pop_front() {
        // hard mode
        if hard {
            state.p_hp -= 1;
            if state.p_hp <= 0 {
                continue;
            }
        }

        // process effects
        state.p_armor = 0;
        if state.shield > 0 {
            state.p_armor = 7;
            state.shield -= 1;
        }
        if state.poison > 0 {
            state.b_hp -= 3;
            state.poison -= 1;
        }
        if state.recharge > 0 {
            state.p_mp += 101;
            state.recharge -= 1;
        }

        // check boss dead
        if state.b_hp <= 0 {
            smallest_mana = smallest_mana.min(state.mana_spent);
            continue;
        }

        // cast spell
        let mana;
        match next_spell {
            Spell::Missile => {
                state.b_hp -= 4;
                mana = 53;
            }
            Spell::Drain => {
                state.b_hp -= 2;
                state.p_hp += 2;
                mana = 73;
            }
            Spell::Shield => {
                mana = 113;
                state.shield = 6;
            }
            Spell::Poison => {
                mana = 173;
                state.poison = 6;
            }
            Spell::Recharge => {
                mana = 229;
                state.recharge = 5;
            }
        }
        state.p_mp -= mana;
        state.mana_spent += mana as usize;

        if state.mana_spent > smallest_mana {
            continue;
        }

        // check boss dead
        if state.b_hp <= 0 {
            smallest_mana = smallest_mana.min(state.mana_spent);
            continue;
        }

        // process effects
        state.p_armor = 0;
        if state.shield > 0 {
            state.p_armor = 7;
            state.shield -= 1;
        }
        if state.poison > 0 {
            state.b_hp -= 3;
            state.poison -= 1;
        }
        if state.recharge > 0 {
            state.p_mp += 101;
            state.recharge -= 1;
        }

        // check boss dead
        if state.b_hp <= 0 {
            smallest_mana = smallest_mana.min(state.mana_spent);
            continue;
        }

        // damage to me
        if state.b_damage > state.p_armor {
            state.p_hp -= state.b_damage - state.p_armor;
        } else {
            state.p_hp -= 1;
        }

        // check if im dead
        if state.p_hp <= 0 {
            continue;
        }

        // queue the next spells
        if state.p_mp >= 53 {
            queue.push_back((state, Spell::Missile));
        }
        if state.p_mp >= 73 {
            queue.push_back((state, Spell::Drain));
        }
        if state.p_mp >= 113 && state.shield <= 1 {
            queue.push_back((state, Spell::Shield));
        }
        if state.p_mp >= 173 && state.poison <= 1 {
            queue.push_back((state, Spell::Poison));
        }
        if state.p_mp >= 229 && state.recharge <= 1 {
            queue.push_back((state, Spell::Recharge));
        }
    }
    smallest_mana
}

fn main() {
    let game = Game {
        p_hp: 50,
        p_mp: 500,
        p_armor: 0,
        b_hp: 71,
        b_damage: 10,
        mana_spent: 0,
        shield: 0,
        poison: 0,
        recharge: 0,
    };

    println!("Part 1: {}", fight(game, false));

    println!("Part 2: {}", fight(game, true));
}
