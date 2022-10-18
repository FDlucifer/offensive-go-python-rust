use std::str::FromStr;

#[derive(Debug, Clone, Copy)]
enum Register {
    A,
    B,
}

impl FromStr for Register {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "a" | "a," => Ok(Self::A),
            "b" | "b," => Ok(Self::B),
            _ => panic!("Unexpected register: {s}"),
         }
    }
}

#[derive(Debug, Clone, Copy)]
enum Instruction {
    Half(Register),
    Triple(Register),
    Increment(Register),
    Jump(isize),
    JumpIfEven(Register, isize),
    JumpIfOne(Register, isize),
}

impl FromStr for Instruction {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut toks = s.split(' ');
        let inst = toks.next().unwrap();
        match inst {
            "jmp" => {
                let dist = toks.next().unwrap().parse().unwrap();
                Ok(Instruction::Jump(dist))
            },
            "hlf" | "tpl" | "inc" => {
                let reg = toks.next().unwrap().parse().unwrap();
                match inst { 
                    "hlf" => Ok(Instruction::Half(reg)),
                    "tpl" => Ok(Instruction::Triple(reg)),
                    "inc" => Ok(Instruction::Increment(reg)),
                    _ => panic!("Unreachable Code"),
                }
            },
            "jie" | "jio" => {
                let reg = toks.next().unwrap().parse().unwrap();
                let offset = toks.next().unwrap().parse().unwrap();
                match inst {
                    "jie" => Ok(Instruction::JumpIfEven(reg, offset)),
                    "jio" => Ok(Instruction::JumpIfOne(reg, offset)),
                    _ => panic!("Unreachable Code"),
                }
            }
            _ => panic!("Unexpected Instruction type: {inst}"),
        }
    }
}

#[derive(Debug)]
struct Computer {
    reg_a: usize,
    reg_b: usize,
    ip: usize,
    insts: Vec<Instruction>,
}

impl Computer {
    fn get(&mut self, reg: Register) -> &mut usize {
        match reg {
            Register::A => &mut self.reg_a,
            Register::B => &mut self.reg_b,
        }
    }

    fn jump(&mut self, off: isize) {
        if off >= 0 {
            self.ip += off as usize;
        } else {
            self.ip -= (-off) as usize;
        }
    }

    fn reset(&mut self, a: usize, b: usize) {
        self.reg_a = a;
        self.reg_b = b;
        self.ip = 0;
    }

    fn run(&mut self) -> usize {
        while self.ip < self.insts.len() {
            let instruction = self.insts[self.ip];
            match instruction {
                Instruction::Half(reg) => {
                    *self.get(reg) /= 2;
                    self.ip += 1;
                },
                Instruction::Triple(reg) => {
                    *self.get(reg) *= 3;
                    self.ip += 1;
                },
                Instruction::Increment(reg) => {
                    *self.get(reg) += 1;
                    self.ip += 1;
                },
                Instruction::Jump(off) => {
                    self.jump(off);
                },
                Instruction::JumpIfEven(reg, off) => {
                    if *self.get(reg) % 2 == 0 {
                        self.jump(off);
                    } else {
                        self.ip += 1;
                    }
                },
                Instruction::JumpIfOne(reg, off) => {
                    if *self.get(reg) == 1 {
                        self.jump(off);
                    } else {
                        self.ip += 1;
                    }
                },
            }
        }
        self.reg_b
    }
}

impl FromStr for Computer {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut insts = Vec::new();
        for line in s.lines() {
            insts.push(line.parse().unwrap());
        }
        Ok(Computer {
            reg_a: 0,
            reg_b: 0,
            ip: 0,
            insts: insts,
        })
    }
}

fn main() {
    let data = include_str!("../input.txt").trim();
    let mut comp: Computer = data.parse().unwrap();
    println!(
        "Part 1: {:?}",
        comp.run()
    );

    comp.reset(1, 0);
    println!(
        "Part 2: {}",
        comp.run()
    );
}