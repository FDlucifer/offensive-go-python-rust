fn get_num() -> u64 {
    5
}

fn inc_num(i: u64) -> u64 {
    i + 1
}

struct Rectangle {
    w: u32,
    h: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.w * self.h
    }
}

fn main() {
    let name: &str = "lUc1f3r11";
    println!("Hello, world!");
    println!("Hello, {}!", name);

    let mut num: u64 = get_num();
    println!("Num: {num}");
    num = inc_num(num);
    println!("New num: {num}");

    for (i, c) in "lUc1f3r11".chars().enumerate() {
        println!("{i}: {c}");
    }

    let r1 = Rectangle {
        w: 4,
        h: 10,
    };

    println!("The rect is {} x {}", r1.w, r1.h);
    println!("It's area is: {}", r1.area());
}
