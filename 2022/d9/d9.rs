use std::collections::HashMap;

fn dist_0(p1: (i32, i32), p2: (i32, i32)) -> i32 {
    i32::max(i32::abs(p1.0 - p2.0), i32::abs(p1.1 - p2.1))
}

fn pos_after_move(head_pos: (i32, i32), tail_pos: (i32, i32), instruction: (i32, i32)) -> ((i32, i32), (i32, i32)) {
    let new_head_pos = (head_pos.0 + instruction.0, head_pos.1 + instruction.1);

    let new_tail_pos = if dist_0(new_head_pos, tail_pos) > 1 {
        let tail_displacement_x = if head_pos.0 - tail_pos.0 > 0 {
            1
        } else if head_pos.0 - tail_pos.0 < 0 {
            -1
        } else {
            0
        };

        let tail_displacement_y = if head_pos.1 - tail_pos.1 > 0 {
            1
        } else if head_pos.1 - tail_pos.1 < 0 {
            -1
        } else {
            0
        };

        (tail_pos.0 + tail_displacement_x, tail_pos.1 + tail_displacement_y)
    } else {
        tail_pos
    };
    
    (new_head_pos, new_tail_pos)
}

fn process_head_movement(head_pos: (i32, i32), tail_pos: (i32, i32), instruction: &str) -> ((i32, i32), (i32, i32)) {
    match instruction {
        "L" => {
            pos_after_move(head_pos, tail_pos, (-1, 0))
        }
        "R" => {
            pos_after_move(head_pos, tail_pos, (1, 0))
        }
        "U" => {
            pos_after_move(head_pos, tail_pos, (0, 1))
        }
        "D" => {
            pos_after_move(head_pos, tail_pos, (0, -1))
        }
        _ => {(head_pos, tail_pos)}
    }
}

fn main() {
    let input: Vec<(&str, u32)> = include_str!("input.txt")
        .trim()
        .split("\n")
        .map(|s| {
            let v : Vec<&str> = s.split_ascii_whitespace().collect();
            (v[0], str::parse::<u32>(v[1]).expect("cannot convert to int"))
        })
        .collect();

    println!("{:?}", input);

    let mut positions : HashMap<(i32, i32), u32> = HashMap::new();
    let mut head_pos = (0, 0);
    let mut tail_pos = (0, 0);
    positions.insert(tail_pos, 1);
    
    for instr in input {
        for _ in 0..(instr.1 as usize) {
            (head_pos, tail_pos) = process_head_movement(head_pos, tail_pos, instr.0);
            println!("{:?}, {:?}", head_pos, tail_pos);
            *positions.entry(tail_pos).or_insert(0) += 1;
        }
    }


    println!("{:?}", positions.keys().len());
}
