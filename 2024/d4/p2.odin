package main

import "core:fmt"

import "core:os"
import "core:strings"
import "core:strconv"
import "core:math"
import "core:slice"

read_file_by_lines_in_whole :: proc(filepath: string) -> [dynamic]string {
	data, ok := os.read_entire_file(filepath, context.allocator)
	if !ok {
		// could not read file
		return {}
	}
	defer delete(data, context.allocator)

	res : [dynamic]string = nil
	it := string(data)
	for line in strings.split_lines_iterator(&it) {
		// process line
		stable_line := strings.clone(strings.trim(line, " \t\n\r\v\f"))
		append(&res, stable_line)
	}

	return res
}

Pos :: struct {
	x : int,
	y : int,
}

// returns all A positions
process_lines :: proc(lines: [dynamic]string) -> [dynamic]Pos {
	a_positions : [dynamic]Pos
	for i in 0..<len(lines) {
		for j in 0..<len(lines[i]) {
			if lines[i][j] == 'A' {
				append(&a_positions, Pos{ i, j })
			}
		}
	}

	return a_positions
}

in_bounds :: proc(board: [dynamic]string, pos: Pos) -> bool {
	return pos.x >= 0 && pos.x < len(board) && pos.y >= 0 && pos.y < len(board[pos.x])
}

has_xmas_at :: proc(board: [dynamic]string, a_position: Pos) -> bool {
	M_count : int = 0
	S_count : int = 0
	offsets := [2]int {-1, 1}
	for offset_x in offsets {
		for offset_y in offsets {
			pos := Pos{a_position.x + offset_x, a_position.y + offset_y}
			if !in_bounds(board, pos) {
				return false
			}

			M_count += board[pos.x][pos.y] == 'M' ? 1 : 0
			S_count += board[pos.x][pos.y] == 'S' ? 1 : 0
		}
	}

	return M_count == 2 && S_count == 2 && board[a_position.x - 1][a_position.y - 1] != board[a_position.x + 1][a_position.y + 1]
}

main :: proc() {
	lines : [dynamic]string = read_file_by_lines_in_whole("input.txt")
	x_positions := process_lines(lines)

	xmas_positions : [dynamic]Pos

	for x_position in x_positions {
		if has_xmas_at(lines, x_position) {
			append(&xmas_positions, x_position)
		}
	}

	fmt.println(xmas_positions)
	fmt.println(len(xmas_positions))
}
