package main

import "core:fmt"
import "core:os"
import "core:strings"

surrounding_balls_around :: proc(diagram: [dynamic]string, i: int, j: int) -> int {
	total := 0
	for x := j - 1; x <= j + 1; x += 1 {
		for y := i - 1; y <= i + 1; y += 1 {
			if y == i && x == j {continue}
			if y < 0 || y >= len(diagram) || x < 0 || x >= len(diagram[y]) {continue}

			total += 1 if diagram[y][x] == '@' else 0
		}
	}

	return total
}

main :: proc() {
	data, ok := os.read_entire_file_from_filename_or_err("input.txt")
	if ok != nil {
		os.exit(1)
	}

	defer delete(data, context.allocator)

	diagram := [dynamic]string{}
	diagram_str := string(data)
	for diagram_row in strings.split_lines_iterator(&diagram_str) {
		append(&diagram, diagram_row)
	}

	total_accesible_balls := 0
	for i := 0; i < len(diagram); i += 1 {
		for j := 0; j < len(diagram[i]); j += 1 {
			if diagram[i][j] == '@' && surrounding_balls_around(diagram, i, j) < 4 {
				total_accesible_balls += 1
			}
		}
	}

	fmt.println(total_accesible_balls)
}
