#!/bin/bash


day=${1##+(0)}
if ((day < 1 || day > 25)); then
    return
fi
    
project=$(printf "day%02d" $1)
if [ -z "$AOC_SESSION" ]; then
    echo "$AOC_SESSION isn't set. Cannot continue."
    exit
fi

cargo new ${project}

cd ${project}

curl -s "https://adventofcode.com/2015/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

echo -n 'fn main() {
    let data = include_str!("../input.txt").trim();
    println!(
        "Part 1: {}",
        ""
    );

    println!(
        "Part 2: {}",
        ""
    );
}' > src/main.rs
