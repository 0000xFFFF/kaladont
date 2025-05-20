use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() -> std::io::Result<()> {
    let file = File::open("dicts/serb.txt")?;
    let reader = BufReader::new(file);

    // Read and filter valid words (length >= 3 characters, not bytes!)
    let valid: Vec<String> = reader
        .lines()
        .filter_map(Result::ok)
        .filter(|line| line.chars().count() >= 3)
        .collect();

    let mut killer = HashSet::new();

    for x in &valid {
        let x_chars: Vec<char> = x.chars().collect();
        let suffix: String = x_chars[x_chars.len() - 2..].iter().collect();

        let found = valid.iter().any(|y| y != x && y.starts_with(&suffix));

        if !found {
            killer.insert(x.clone());
            println!("{}", x);
        }
    }

    Ok(())
}

