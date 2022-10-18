use regex::Regex;

fn main() {
    let data = include_str!("../input.txt");
    let hex_regex = Regex::new(r"\\x[a-f0-9A-F]{2}").unwrap();

    let mut num_code = 0;
    let mut num_string = 0;
    let mut num_encoded = 0;
    for line in data.lines() {
        num_code += line.len();
        num_string += hex_regex
            .replace_all(line, "x")
            .replace("\\\\", "x")
            .replace("\\\"", "x").len() - 2;
        num_encoded += line.len() + line.matches("\\").count() + line.matches("\"").count() + 2;
    }

    println!(
        "Part 1: {}",
        num_code - num_string
    );

    println!(
        "Part 2: {}",
        num_encoded - num_code
    );
}