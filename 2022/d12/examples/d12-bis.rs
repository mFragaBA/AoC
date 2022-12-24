use std::collections::VecDeque;

fn in_grid(pos: (i32, i32), height: usize, width: usize) -> bool {
    pos.0 >= 0 && pos.1 >= 0 && pos.0 < height as i32 && pos.1 < width as i32
}

fn print_path(start: (usize, usize), end: (usize, usize), dist: &Vec<Vec<usize>>) {
    let mut current = end;
    let mut current_dist = dist[end.0][end.1];
    let mut grid = vec![vec!['.'; dist[0].len()]; dist.len()];
    grid[start.0][start.1] = 'S';
    grid[end.0][end.1] = 'E';
    while current != start {
        println!("current: {:?}", current);
        let above = (current.0 as i32 - 1, current.1 as i32);
        let below = (current.0 as i32 + 1, current.1 as i32);
        let left = (current.0 as i32, current.1 as i32 - 1);
        let right = (current.0 as i32, current.1 as i32 + 1);

        if in_grid(above, dist.len(), dist[0].len()) && dist[above.0 as usize][above.1 as usize] + 1 == current_dist {
            current = (above.0 as usize, above.1 as usize);
            grid[current.0][current.1] = 'v';
        } else if in_grid(below, dist.len(), dist[0].len()) && dist[below.0 as usize][below.1 as usize] + 1 == current_dist {
            current = (below.0 as usize, below.1 as usize);
            grid[current.0][current.1] = '^';
        } else if in_grid(left, dist.len(), dist[0].len()) && dist[left.0 as usize][left.1 as usize] + 1 == current_dist {
            current = (left.0 as usize, left.1 as usize);
            grid[current.0][current.1] = '>';
        } else if in_grid(right, dist.len(), dist[0].len()) && dist[right.0 as usize][right.1 as usize] + 1 == current_dist {
            current = (right.0 as usize, right.1 as usize);
            grid[current.0][current.1] = '<';
        }

        // println!("{:?}-{}", current, current_dist);
        current_dist -= 1;
    }
    for row in grid.iter() {
        println!("{}", row.into_iter().collect::<String>());
    }
}

fn maybe_add_node_to_queue(
    q: &mut VecDeque<((usize, usize), usize)>, 
    grid_str: &Vec<Vec<char>>, 
    from: (usize, usize), 
    to: (usize, usize),
    dist: usize
) {
    // println!("from: {:?} = {} = {}", from, grid_str[from.0][from.1], grid_str[from.0][from.1] as i32);
    // println!("to: {:?} = {} = {}", to, grid_str[to.0][to.1], grid_str[to.0][to.1] as i32);
    if grid_str[from.0][from.1] as usize + 1 >= grid_str[to.0][to.1] as usize {
        q.push_back((to, dist));
    }
}

fn main() {
    // Read input
    let mut grid_str : Vec<Vec<char>>= include_str!("../input.txt")
        .trim()
        .split_ascii_whitespace()
        .map(|line| line.chars().collect())
        .collect();

    println!("{:?}", grid_str);

    // Mark start and end positions
    let mut start = (0,0);
    let mut end = (0,0);

    for (idx, c) in grid_str.iter().flatten().enumerate() {
        if *c == 'S' {
            let x = idx / grid_str[0].len();
            let y = idx % grid_str[0].len();
            start = (x, y)
        }

        if *c == 'E' {
            let x = idx / grid_str[0].len();
            let y = idx % grid_str[0].len();
            end = (x, y)
        }
    }

    println!("{:?}", start);
    println!("{:?}", end);

    // Set the correct elevation for start and end
    grid_str[start.0][start.1] = 'a';
    grid_str[end.0][end.1] = 'z';

    // Find all possible starts
    let possible_starts : Vec<(usize, usize)> = grid_str
        .iter()
        .flatten()
        .enumerate()
        .filter(|(_idx, c)| **c == 'a')
        .map(|(idx, _c)| (idx / grid_str[0].len(), idx % grid_str[0].len()))
        .collect();

    let mut min_dist = grid_str[0].len() * grid_str.len();
    for start in possible_starts {

        // Initialize BFS data
        let mut visited : Vec<Vec<bool>> = vec![vec![false; grid_str[0].len()]; grid_str.len()];
        let mut queue = VecDeque::<((usize, usize), usize)>::with_capacity(grid_str.len() * grid_str[0].len());
        let mut distance_to_start : Vec<Vec<usize>> =vec![vec![visited.len() * visited[0].len(); grid_str[0].len()]; grid_str.len()]; 
        distance_to_start[start.0][start.1] = 0;

        let mut grid = vec![vec!['.'; grid_str[0].len()]; grid_str.len()];
        grid[start.0][start.1] = 'S';
        grid[end.0][end.1] = 'E';


        // BFS
        queue.push_back((start, 0));
        while !queue.is_empty() {
            let ((node_x, node_y), dist) = queue.pop_front().unwrap();
            if visited[node_x][node_y] { continue; }

            let above = (node_x as i32 - 1, node_y as i32);
            let below = (node_x as i32 + 1, node_y as i32);
            let left = (node_x as i32, node_y as i32 - 1);
            let right = (node_x as i32, node_y as i32 + 1);

            // println!("visiting: {:?}", (node_x, node_y));

            visited[node_x][node_y] = true;
            distance_to_start[node_x][node_y] = dist;
            grid[node_x][node_y] = '*';

            if in_grid(above, grid_str.len(), grid_str[0].len()) {
                maybe_add_node_to_queue(&mut queue, &grid_str, (node_x, node_y), (above.0 as usize, above.1 as usize), dist + 1);
            }
            if in_grid(below, grid_str.len(), grid_str[0].len()) {
                maybe_add_node_to_queue(&mut queue, &grid_str, (node_x, node_y), (below.0 as usize, below.1 as usize), dist + 1);
            }
            if in_grid(left, grid_str.len(), grid_str[0].len()) {
                maybe_add_node_to_queue(&mut queue, &grid_str, (node_x, node_y), (left.0 as usize, left.1 as usize), dist + 1);
            }
            if in_grid(right, grid_str.len(), grid_str[0].len()) {
                maybe_add_node_to_queue(&mut queue, &grid_str, (node_x, node_y), (right.0 as usize, right.1 as usize), dist + 1);
            }

            // let ten_millis = std::time::Duration::from_millis(1);
            // std::thread::sleep(ten_millis);
            // print!("{}[2J", 27 as char);
            // for row in grid.iter() {
            //     println!("{}", row.into_iter().collect::<String>());
            // }
        }

        if distance_to_start[end.0][end.1] < grid_str.len() * grid_str[0].len() {
            let ten_millis = std::time::Duration::from_millis(100);
            std::thread::sleep(ten_millis);
            print_path(start, end, &distance_to_start);
        }

        // println!("dist to end: {}", distance_to_start[end.0][end.1]);
        min_dist = usize::min(min_dist, distance_to_start[end.0][end.1]);
    }
    println!("min_dist: {}", min_dist);
}
