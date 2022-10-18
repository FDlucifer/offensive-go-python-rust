struct Present {
    l: u32,
    w: u32,
    h: u32,
}

impl Present {
    /*fn new(l: u32, w: u32, h: u32) -> Self{
        Present { l, w, h }
    }*/

    fn paper_needed(&self) -> u32 {
        (3 * self.l * self.w) + (2 * self.l * self.h) + (2 * self.h * self.w)
    }

    fn ribbon_needed(&self) -> u32 {
        2*self.l + 2*self.w + self.l*self.w*self.h
    }
}

impl From<Vec<u32>> for Present {
    fn from(vec: Vec<u32>) -> Present {
        Present {
            l: vec[0],
            w: vec[1],
            h: vec[2],
        }
    }
}

fn main() {
    let data = include_str!("../input.txt");

    let mut total_area = 0;
    let mut total_ribbon = 0;

    for line in data.lines() {
        let mut dims: Vec<u32> = line
            .split('x')
            .map(|d| d.parse().expect("parse error"))
            .collect();
        dims.sort();

        //let p = Present {
        //    l: dims[0],
        //    w: dims[1],
        //    h: dims[2],
        //};
        //let p = Present::new(dims[0], dims[1], dims[2]);
        let p: Present = dims.into();
        total_area += p.paper_needed();
        total_ribbon += p.ribbon_needed();
    }
    println!(
        "Part 1: {}",
        total_area
    );

    println!(
        "Part 2: {}",
        total_ribbon
    );
}