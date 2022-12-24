use std::collections::HashMap;

fn dist_0(p1: (i32, i32), p2: (i32, i32)) -> i32 {
    i32::max(i32::abs(p1.0 - p2.0), i32::abs(p1.1 - p2.1))
}

fn adjust_knot(parent_knot: (i32, i32), child_knot: (i32, i32)) -> (i32, i32) {
    if dist_0(parent_knot, child_knot) > 1 {
        let tail_displacement_x = if parent_knot.0 - child_knot.0 > 0 {
            1
        } else if parent_knot.0 - child_knot.0 < 0 {
            -1
        } else {
            0
        };

        let tail_displacement_y = if parent_knot.1 - child_knot.1 > 0 {
            1
        } else if parent_knot.1 - child_knot.1 < 0 {
            -1
        } else {
            0
        };

        (child_knot.0 + tail_displacement_x, child_knot.1 + tail_displacement_y)
    } else {
        child_knot
    }
}


fn pos_after_move(rope: &mut [(i32, i32)], instruction: (i32, i32)) {
    rope[0] = (rope[0].0 + instruction.0, rope[0].1 + instruction.1);

    for i in 1..rope.len() {
        rope[i] = adjust_knot(rope[i-1], rope[i]);
    }
    
}

fn process_head_movement(rope: &mut[(i32, i32)], instruction: &str) {
    match instruction {
        "L" => {
            pos_after_move(rope, (-1, 0))
        }
        "R" => {
            pos_after_move(rope, (1, 0))
        }
        "U" => {
            pos_after_move(rope, (0, 1))
        }
        "D" => {
            pos_after_move(rope, (0, -1))
        }
        _ => {}
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
    let mut rope : Vec<(i32, i32)> = vec![(0,0); 10];
    positions.insert(rope[9], 1);
    
    for instr in input {
        for _ in 0..(instr.1 as usize) {
            process_head_movement(&mut rope, instr.0);
            *positions.entry(rope[9]).or_insert(0) += 1;
        }
    }


    println!("{:?}", positions.keys().len());
}
