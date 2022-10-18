fn main() {
    let data = include_str!("../input.txt");

    println!(
        "Part 1: {}",
        data.len() - 2*(data.matches(')').count())
    );

    let mut floor = 0;
    for (i, c) in data.chars().enumerate() {
        match c {
            '(' => floor += 1,
            ')' => floor -= 1,
            _   => {
                let cbyte = c as u8;
                panic!("unexpected character {c} [0x{cbyte:02x}]");
            },
        }
        if floor < 0 {
            println!(
                "Part 2: {}",
                i + 1
            );
            break;
        }
    }
}