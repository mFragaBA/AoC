package main

import "core:fmt"
import "core:os"
import "core:strings"

surrounding_balls_around :: proc(diagram: [dynamic][dynamic]rune, i: int, j: int) -> int {
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

	diagram := [dynamic][dynamic]rune{}
	next_diagram_state := [dynamic][dynamic]rune{}
	diagram_str := string(data)
	for diagram_row in strings.split_lines_iterator(&diagram_str) {
		row := [dynamic]rune{}
		for rune in diagram_row {
			append(&row, rune)
		}
		append(&diagram, row)
	}
	next_diagram_state = diagram

	total_removable_balls := 0
	has_removed := true

	for has_removed {
		has_removed = false
		for i := 0; i < len(diagram); i += 1 {
			for j := 0; j < len(diagram[i]); j += 1 {
				if diagram[i][j] == '@' && surrounding_balls_around(diagram, i, j) < 4 {
					total_removable_balls += 1
					next_diagram_state[i][j] = '.'
					has_removed = true
				} else {
					next_diagram_state[i][j] = diagram[i][j]
				}
			}
		}

		diagram = next_diagram_state
		fmt.println("Next State: ")

		for row in diagram {
			fmt.println(row)
		}
	}

	fmt.println(total_removable_balls)
}
